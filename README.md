# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_12:33:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 12:33:52 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.025 |  |
| 2026-10-23 12:09:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-23 12:09:08 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | -0.019 |  |
| 2026-10-23 12:07:26 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 12:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.05 | 🟡 Alert | -0.030 |  |
| 2026-10-23 12:01:11 | Moragaswewa (Deduru Oya) | 4.75 | 🟡 Alert | -0.040 |  |
| 2026-10-23 12:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-23 12:09:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-23 12:03:08 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-23 12:02:13 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 12:01:29 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 12:02:14 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 12:01:13 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-23 12:03:17 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-23 12:03:21 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 12:04:44 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-23 12:00:59 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-23 12:01:10 | Thanthirimale (Malwathu Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-10-23 12:06:37 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 12:01:23 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-23 12:05:25 | Galgamuwa (Mee Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-10-23 12:01:08 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-23 12:07:26 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-10-23 12:04:42 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.013 |  |
| 2026-10-23 12:04:31 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-10-23 12:09:08 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | -0.019 |  |
| 2026-10-23 12:03:04 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-10-23 12:02:22 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-10-23 12:01:03 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-23 12:02:03 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-23 12:33:52 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.025 |  |
| 2026-10-23 12:06:22 | Glencourse (Kelani Ganga) | 11.48 | 🟢 Normal | -0.029 |  |
| 2026-10-23 12:05:26 | Giriulla (Maha Oya) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-10-23 12:00:58 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.031 |  |
| 2026-10-23 12:06:27 | Ellagawa (Kalu Ganga) | 7.59 | 🟢 Normal | -0.037 |  |
| 2026-10-23 12:06:49 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.039 |  |
| 2026-10-23 12:04:48 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-10-23 12:01:41 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.040 |  |
| 2026-10-23 12:04:48 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.050 |  |
| 2026-10-23 12:02:53 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.055 |  |
| 2026-10-23 12:03:10 | Hanwella (Kelani Ganga) | 4.06 | 🟢 Normal | -0.061 |  |
| 2026-10-23 12:02:26 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.065 |  |
| 2026-10-23 12:02:02 | Rathnapura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)