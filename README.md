# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_04:02:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,638 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 04:02:58 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-31 04:02:57 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | -0.121 |  |
| 2026-10-31 04:02:37 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:30 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.049 |  |
| 2026-10-31 04:02:27 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 04:02:15 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:11 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:10 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:00:58 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2026-10-31 04:00:56 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:00:49 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-31 03:56:39 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 04:00:49 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-31 03:06:07 | Panadugama (Nilwala Ganga) | 5.02 | 🟡 Alert | -0.016 |  |
| 2026-10-31 03:05:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -3.130 |  |
| 2026-10-31 03:05:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.485 | 🔺 Rising |
| 2026-10-31 03:03:51 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-31 03:11:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-31 04:02:58 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-31 04:02:10 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 04:02:27 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 02:04:23 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-31 04:00:56 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:37 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:56:39 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:15 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:04:00 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:10:35 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:02:11 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:11:39 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-31 04:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-31 03:02:26 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-31 03:02:09 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-10-31 03:05:38 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-31 03:03:41 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-31 03:05:39 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-31 03:03:02 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.021 |  |
| 2026-10-31 04:00:58 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2026-10-31 03:06:28 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.029 |  |
| 2026-10-31 03:11:45 | Rathnapura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.030 |  |
| 2026-10-31 03:07:42 | Baddegama (Gin Ganga) | 2.87 | 🟢 Normal | -0.032 |  |
| 2026-10-31 03:08:42 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | -0.037 |  |
| 2026-10-31 03:01:08 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.042 |  |
| 2026-10-31 04:02:30 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.049 |  |
| 2026-10-31 03:06:32 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.055 |  |
| 2026-10-31 04:02:57 | Ellagawa (Kalu Ganga) | 7.38 | 🟢 Normal | -0.121 |  |
| 2026-10-31 03:09:54 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -252.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)