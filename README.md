# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_14:12:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,241 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 14:12:38 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:12:27 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-06-23 14:09:49 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.076 |  |
| 2026-06-23 14:09:45 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:08:19 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:08:07 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.049 |  |
| 2026-06-23 14:07:44 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.100 |  |
| 2026-06-23 14:07:04 | Dunamale (Aththanagalu Oya) | 4.05 | 🟡 Alert | -0.028 |  |
| 2026-06-23 14:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | 0.000 |  |
| 2026-06-23 14:06:34 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.162 |  |
| 2026-06-23 14:06:15 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-23 14:06:10 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | -0.047 |  |
| 2026-06-23 14:05:20 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:04:08 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-06-23 14:03:42 | Hanwella (Kelani Ganga) | 4.55 | 🟢 Normal | -0.130 |  |
| 2026-06-23 14:03:23 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:03:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:03:14 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:03:02 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | -0.066 |  |
| 2026-06-23 14:02:53 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:02:46 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:02:42 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:02:36 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-23 14:02:26 | Giriulla (Maha Oya) | 2.38 | 🟢 Normal | -0.049 |  |
| 2026-06-23 14:02:26 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | -0.036 |  |
| 2026-06-23 14:02:19 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-23 14:02:11 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-06-23 14:02:10 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:02:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:02:04 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:01:57 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:01:43 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:01:35 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:01:24 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 14:01:24 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:01:24 | Nagalagam Street (Kelani Ganga) | 0.81 | 🟢 Normal | -0.015 |  |
| 2026-06-23 14:00:19 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:00:07 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 14:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | 0.000 |  |
| 2026-06-23 14:07:04 | Dunamale (Aththanagalu Oya) | 4.05 | 🟡 Alert | -0.028 |  |
| 2026-06-23 14:02:19 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-23 14:01:24 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 14:02:36 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-23 14:01:35 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:00:07 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:02:42 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:02:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:02:53 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:02:46 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:03:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:02:04 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:03:14 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:01:24 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:03:23 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:05:20 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:12:38 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:08:19 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 14:01:43 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:01:37 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:09:45 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:01:57 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:02:10 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:00:19 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-23 14:01:24 | Nagalagam Street (Kelani Ganga) | 0.81 | 🟢 Normal | -0.015 |  |
| 2026-06-23 14:12:27 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-06-23 14:06:15 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-23 14:02:11 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-06-23 14:04:08 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.030 |  |
| 2026-06-23 14:02:26 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | -0.036 |  |
| 2026-06-23 14:06:10 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | -0.047 |  |
| 2026-06-23 14:02:26 | Giriulla (Maha Oya) | 2.38 | 🟢 Normal | -0.049 |  |
| 2026-06-23 14:08:07 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.049 |  |
| 2026-06-23 14:03:02 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | -0.066 |  |
| 2026-06-23 14:09:49 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.076 |  |
| 2026-06-23 14:07:44 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.100 |  |
| 2026-06-23 14:03:42 | Hanwella (Kelani Ganga) | 4.55 | 🟢 Normal | -0.130 |  |
| 2026-06-23 14:06:34 | Glencourse (Kelani Ganga) | 11.82 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)