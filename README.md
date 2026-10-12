# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_06:34:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **1** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 06:34:28 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.002 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 06:05:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | 0.088 | 🔺 Rising |
| 2026-10-12 06:09:39 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-10-12 06:00:34 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-12 06:09:20 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-12 06:05:30 | Badalgama (Maha Oya) | 3.77 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 06:06:15 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 06:01:46 | Ellagawa (Kalu Ganga) | 7.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 06:04:24 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 06:02:01 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 06:34:28 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.002 |  |
| 2026-10-12 06:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-12 06:09:56 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 06:09:13 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 06:04:00 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 06:00:16 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 06:03:02 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-10-12 06:04:21 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-12 06:01:09 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-12 06:06:40 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-10-12 06:03:09 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-10-12 06:03:09 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-12 06:02:46 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.011 |  |
| 2026-10-12 06:05:34 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.012 |  |
| 2026-10-12 05:01:15 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-12 06:04:38 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-10-12 06:07:18 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | -0.028 |  |
| 2026-10-12 06:02:56 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-10-12 06:02:26 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.043 |  |
| 2026-10-12 06:02:20 | Magura (Kalu Ganga) | 3.00 | 🟢 Normal | -0.044 |  |
| 2026-10-12 06:07:00 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.048 |  |
| 2026-10-12 06:08:23 | Panadugama (Nilwala Ganga) | 4.94 | 🟢 Normal | -0.054 |  |
| 2026-10-12 06:02:46 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.081 |  |
| 2026-10-12 06:03:49 | Moragaswewa (Deduru Oya) | 1.17 | 🟢 Normal | -0.087 |  |
| 2026-10-12 06:09:36 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.108 |  |
| 2026-10-12 06:03:10 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.139 |  |
| 2026-10-12 06:02:58 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | -0.149 |  |
| 2026-10-12 06:03:58 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.269 |  |
| 2026-10-12 06:01:06 | Thawalama (Gin Ganga) | 2.90 | 🟢 Normal | -0.285 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)