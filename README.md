# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_06:18:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,829 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 06:18:00 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.001 |  |
| 2026-06-24 06:13:30 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:10:47 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.017 |  |
| 2026-06-24 06:08:39 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.033 |  |
| 2026-06-24 06:08:10 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:07:12 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-24 06:06:40 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-06-24 06:06:14 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:05:56 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:05:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:05:46 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:05:37 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-06-24 06:05:22 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 06:04:46 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.145 |  |
| 2026-06-24 06:04:30 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | -0.145 |  |
| 2026-06-24 06:04:12 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:04:06 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-06-24 06:04:05 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.044 |  |
| 2026-06-24 06:03:55 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.047 |  |
| 2026-06-24 06:03:38 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | 0.004 |  |
| 2026-06-24 06:03:36 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 06:03:19 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.047 |  |
| 2026-06-24 06:03:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:02:44 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.012 |  |
| 2026-06-24 06:02:36 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-24 06:02:32 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.080 |  |
| 2026-06-24 06:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | -0.132 |  |
| 2026-06-24 06:02:22 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.032 |  |
| 2026-06-24 06:02:20 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-24 06:02:18 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:01:49 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 06:01:42 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-24 06:01:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:01:34 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:01:29 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.064 |  |
| 2026-06-24 06:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-06-24 06:01:15 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.023 |  |
| 2026-06-24 06:00:51 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:00:08 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -4.212 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 06:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | -0.132 |  |
| 2026-06-24 06:05:37 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-06-24 06:07:12 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-24 06:01:42 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-24 06:01:49 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 06:05:22 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 06:03:36 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 06:03:38 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | 0.004 |  |
| 2026-06-24 06:18:00 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.001 |  |
| 2026-06-24 06:01:34 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:00:51 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:01:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:08:10 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:04:12 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:05:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:02:18 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:06:14 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:05:56 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:03:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:13:30 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 06:02:36 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-24 06:06:40 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-06-24 06:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-06-24 06:02:44 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.012 |  |
| 2026-06-24 06:10:47 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.017 |  |
| 2026-06-24 06:04:06 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-06-24 06:01:15 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.023 |  |
| 2026-06-24 06:02:22 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.032 |  |
| 2026-06-24 06:08:39 | Rathnapura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.033 |  |
| 2026-06-24 06:04:05 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.044 |  |
| 2026-06-24 06:03:19 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.047 |  |
| 2026-06-24 06:03:55 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.047 |  |
| 2026-06-24 06:01:29 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.064 |  |
| 2026-06-24 06:02:20 | Dunamale (Aththanagalu Oya) | 3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-24 06:02:32 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.080 |  |
| 2026-06-24 06:04:30 | Ellagawa (Kalu Ganga) | 7.05 | 🟢 Normal | -0.145 |  |
| 2026-06-24 06:04:46 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.145 |  |
| 2026-06-24 06:00:08 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -4.212 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)