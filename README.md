# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_15:27:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,757 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 15:27:09 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:20:34 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:12:10 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:10:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-14 15:10:11 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-14 15:08:57 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.029 |  |
| 2026-09-14 15:08:12 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:08:11 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:06:40 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -36.000 |  |
| 2026-09-14 15:06:39 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -36.000 |  |
| 2026-09-14 15:05:27 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:05:14 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:04:50 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:04:40 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:04:35 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-14 15:04:33 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.029 |  |
| 2026-09-14 15:04:20 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-14 15:04:17 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:04:02 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:03:55 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:03:44 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.012 |  |
| 2026-09-14 15:03:44 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:03:43 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:03:43 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.023 |  |
| 2026-09-14 15:03:10 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:03:07 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-09-14 15:03:05 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:02:56 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:02:47 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.041 |  |
| 2026-09-14 15:02:45 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-09-14 15:02:45 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-09-14 15:02:25 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:02:25 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:02:16 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:02:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:01:59 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:01:54 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:01:41 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 15:01:27 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 15:10:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-14 15:04:20 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-14 15:10:11 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-14 15:04:35 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-14 15:01:41 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 15:02:16 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:02:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:04:40 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:05:14 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:03:10 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:27:09 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:04:50 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:20:34 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:12:10 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:03:43 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:01:59 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:02:56 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:04:02 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:02:25 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:03:55 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:03:05 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:02:25 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-14 15:05:27 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:03:44 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:02:45 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:01:27 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:08:12 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:04:17 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-09-14 15:03:07 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-09-14 15:03:44 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.012 |  |
| 2026-09-14 15:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-09-14 15:03:43 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.023 |  |
| 2026-09-14 15:08:57 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.029 |  |
| 2026-09-14 15:04:33 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.029 |  |
| 2026-09-14 15:02:45 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-09-14 15:02:47 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.041 |  |
| 2026-09-14 14:07:13 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-09-14 15:06:40 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)