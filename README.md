# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_07:04:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,190 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 07:04:14 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-06 07:04:08 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 07:04:02 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-06 07:03:56 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-11-06 07:03:36 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:03:35 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.041 |  |
| 2026-11-06 07:03:27 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 07:03:23 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.032 |  |
| 2026-11-06 07:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.43 | 🟢 Normal | -0.030 |  |
| 2026-11-06 07:03:14 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-11-06 07:02:51 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.010 |  |
| 2026-11-06 07:02:48 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 07:02:25 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:02:15 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:02:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.021 |  |
| 2026-11-06 07:02:03 | Putupaula (Kalu Ganga) | 1.24 | 🟢 Normal | -0.100 |  |
| 2026-11-06 07:01:57 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.147 |  |
| 2026-11-06 07:01:56 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-06 07:01:22 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:01:19 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | -144.000 |  |
| 2026-11-06 07:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:00:54 | Giriulla (Maha Oya) | 2.79 | 🟢 Normal | -144.000 |  |
| 2026-11-06 07:00:52 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.012 |  |
| 2026-11-06 07:00:38 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.081 |  |
| 2026-11-06 07:00:25 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-06 06:50:06 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.015 |  |
| 2026-11-06 06:36:42 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 07:00:25 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-06 07:03:27 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-06 07:04:02 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-06 06:08:39 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-06 07:02:48 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 07:04:08 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 07:02:25 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:09:51 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:03:36 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:01:22 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:06:10 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 06:03:38 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 07:02:15 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:52:19 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2026-11-06 07:04:14 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-11-06 07:02:51 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.010 |  |
| 2026-11-06 06:05:40 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-06 07:01:56 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-06 07:00:52 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.012 |  |
| 2026-11-06 06:50:06 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.015 |  |
| 2026-11-06 07:03:56 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-11-06 06:11:10 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-06 07:02:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.021 |  |
| 2026-11-06 07:03:14 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-11-06 07:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.43 | 🟢 Normal | -0.030 |  |
| 2026-11-06 06:02:58 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.030 |  |
| 2026-11-06 07:03:23 | Hanwella (Kelani Ganga) | 2.39 | 🟢 Normal | -0.032 |  |
| 2026-11-06 06:03:11 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-11-06 07:03:35 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.041 |  |
| 2026-11-06 06:02:52 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.044 |  |
| 2026-11-06 06:07:32 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.076 |  |
| 2026-11-06 07:00:38 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.081 |  |
| 2026-11-06 06:09:35 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.085 |  |
| 2026-11-06 07:02:03 | Putupaula (Kalu Ganga) | 1.24 | 🟢 Normal | -0.100 |  |
| 2026-11-06 07:01:57 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.147 |  |
| 2026-11-06 06:02:52 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.153 |  |
| 2026-11-06 06:03:40 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -1.055 |  |
| 2026-11-06 07:01:19 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)