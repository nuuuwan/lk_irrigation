# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_14:02:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,463 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 14:02:56 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:02:55 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-06 14:02:48 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:02:41 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 14:02:34 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 14:02:15 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:02:13 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-11-06 14:01:48 | Thanthirimale (Malwathu Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 14:01:46 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.021 |  |
| 2026-11-06 14:01:35 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.088 |  |
| 2026-11-06 14:01:22 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.014 |  |
| 2026-11-06 14:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-06 14:01:13 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-11-06 14:01:09 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:00:56 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:00:56 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:00:50 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-06 14:00:23 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-06 13:59:05 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:17:00 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 14:00:50 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-06 14:00:23 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-06 14:02:34 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 14:02:41 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 14:01:48 | Thanthirimale (Malwathu Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 13:01:33 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 14:00:56 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:38 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:02:53 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:04:14 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:39 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:01:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:01:09 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:02:15 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:02:48 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:02:58 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:14:29 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:03:05 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:00:56 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 13:05:34 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:02:56 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-06 14:02:55 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-06 13:05:58 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-11-06 14:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-06 14:02:13 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-11-06 13:03:43 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-11-06 14:01:22 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.014 |  |
| 2026-11-06 13:07:56 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-11-06 14:01:13 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-11-06 14:01:46 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.021 |  |
| 2026-11-06 13:05:15 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.021 |  |
| 2026-11-06 13:05:14 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.028 |  |
| 2026-11-06 13:06:56 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.028 |  |
| 2026-11-06 13:06:22 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | -0.038 |  |
| 2026-11-06 13:02:04 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.041 |  |
| 2026-11-06 13:04:28 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.050 |  |
| 2026-11-06 13:05:02 | Moragaswewa (Deduru Oya) | 2.77 | 🟢 Normal | -0.057 |  |
| 2026-11-06 13:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | -0.062 |  |
| 2026-11-06 14:01:35 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)