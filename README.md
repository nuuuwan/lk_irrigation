# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_20:34:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,608 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 20:34:23 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:22:01 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.026 |  |
| 2026-11-25 20:18:09 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:17:59 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.012 |  |
| 2026-11-25 20:16:07 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:15:09 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-11-25 20:10:28 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-25 20:10:14 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.018 |  |
| 2026-11-25 20:09:43 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.019 |  |
| 2026-11-25 20:08:45 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | -0.145 |  |
| 2026-11-25 20:07:31 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-11-25 20:07:26 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 20:06:36 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.037 |  |
| 2026-11-25 20:06:25 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:06:18 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-11-25 20:06:00 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:05:34 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-11-25 20:04:30 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | 0.499 | 🔺 Rising |
| 2026-11-25 20:04:27 | Peradeniya (Mahaweli Ganga) | 5.27 | 🟡 Alert | 0.775 | 🔺 Rising |
| 2026-11-25 20:04:15 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | -0.081 |  |
| 2026-11-25 20:04:04 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-25 20:04:02 | Dunamale (Aththanagalu Oya) | 3.16 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-11-25 20:03:53 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.039 |  |
| 2026-11-25 20:03:10 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:02:58 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.060 |  |
| 2026-11-25 20:02:55 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:02:55 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.144 |  |
| 2026-11-25 20:02:51 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-25 20:02:20 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:02:17 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.072 |  |
| 2026-11-25 20:02:11 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-25 20:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.059 |  |
| 2026-11-25 20:01:26 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | -0.032 |  |
| 2026-11-25 20:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-25 20:00:20 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.064 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 20:04:27 | Peradeniya (Mahaweli Ganga) | 5.27 | 🟡 Alert | 0.775 | 🔺 Rising |
| 2026-11-25 20:04:30 | Glencourse (Kelani Ganga) | 11.13 | 🟢 Normal | 0.499 | 🔺 Rising |
| 2026-11-25 20:05:34 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-11-25 20:04:02 | Dunamale (Aththanagalu Oya) | 3.16 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-11-25 20:15:09 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-11-25 18:02:46 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-25 20:02:11 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-25 20:04:04 | Moragaswewa (Deduru Oya) | 1.43 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-25 18:02:35 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-25 20:10:28 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-25 20:02:51 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-25 18:00:42 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-25 20:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-25 20:07:26 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 20:02:55 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:34:23 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:02:20 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:06:25 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:03:10 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:18:09 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:06:00 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:16:07 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-25 20:17:59 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.012 |  |
| 2026-11-25 20:10:14 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | -0.018 |  |
| 2026-11-25 20:06:18 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-11-25 20:09:43 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.019 |  |
| 2026-11-25 20:07:31 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 20:22:01 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.026 |  |
| 2026-11-25 20:01:26 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | -0.032 |  |
| 2026-11-25 20:06:36 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.037 |  |
| 2026-11-25 20:03:53 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.039 |  |
| 2026-11-25 20:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.059 |  |
| 2026-11-25 20:02:58 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.060 |  |
| 2026-11-25 20:00:20 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.064 |  |
| 2026-11-25 20:02:17 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.072 |  |
| 2026-11-25 20:04:15 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | -0.081 |  |
| 2026-11-25 20:02:55 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.144 |  |
| 2026-11-25 20:08:45 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)