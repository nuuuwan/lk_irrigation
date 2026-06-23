# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_04:20:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,749 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 04:20:32 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.008 |  |
| 2026-06-24 04:18:57 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:15:07 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:11:43 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.035 |  |
| 2026-06-24 04:10:32 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:09:00 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:08:10 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.053 |  |
| 2026-06-24 04:07:30 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:06:11 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-24 04:05:32 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.030 |  |
| 2026-06-24 04:05:02 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.059 |  |
| 2026-06-24 04:04:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:04:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 04:03:43 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-24 04:03:10 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-06-24 04:02:53 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:02:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:02:45 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:02:40 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.169 |  |
| 2026-06-24 04:02:40 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | -0.060 |  |
| 2026-06-24 04:01:55 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:01:53 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.040 |  |
| 2026-06-24 04:01:50 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:01:28 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.052 |  |
| 2026-06-24 04:01:15 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:01:14 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:01:10 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-24 04:01:03 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-24 04:00:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.72 | 🟡 Alert | -0.020 |  |
| 2026-06-24 04:00:42 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.371 |  |
| 2026-06-24 04:00:42 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 04:00:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.72 | 🟡 Alert | -0.020 |  |
| 2026-06-24 04:02:40 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | -0.060 |  |
| 2026-06-24 04:03:43 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-24 04:01:03 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-24 04:01:10 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-24 04:04:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 04:00:42 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:01:14 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:02:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:01:55 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:02:45 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:02:53 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:15:07 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:04:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:09:00 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:01:15 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:07:30 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:18:57 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:13:07 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:10:32 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:01:50 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:20:32 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.008 |  |
| 2026-06-24 03:09:14 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-24 04:06:11 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-24 03:01:31 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-06-24 04:05:32 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.030 |  |
| 2026-06-24 04:11:43 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.035 |  |
| 2026-06-24 04:01:53 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.040 |  |
| 2026-06-24 04:03:10 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.040 |  |
| 2026-06-24 03:00:34 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.045 |  |
| 2026-06-24 04:01:28 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.052 |  |
| 2026-06-24 04:08:10 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.053 |  |
| 2026-06-24 04:05:02 | Glencourse (Kelani Ganga) | 10.89 | 🟢 Normal | -0.059 |  |
| 2026-06-24 03:35:15 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.106 |  |
| 2026-06-24 04:02:40 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.169 |  |
| 2026-06-24 04:00:42 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.371 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)