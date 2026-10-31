# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_16:02:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,098 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 16:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 16:02:52 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.081 |  |
| 2026-10-31 16:02:48 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:43 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | -0.011 |  |
| 2026-10-31 16:02:32 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:02:23 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 16:02:16 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:12 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:01:31 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-31 16:01:24 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-31 16:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:00:08 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:59:04 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 16:02:43 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | -0.011 |  |
| 2026-10-31 16:01:31 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-31 16:02:23 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 16:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-31 15:01:07 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-31 15:00:56 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 15:06:22 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:48 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-31 15:01:49 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:16 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:12 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-31 16:02:32 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:01:29 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:00:08 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:02:53 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:01:14 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:01:15 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-10-31 16:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:04:00 | Galgamuwa (Mee Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-31 15:06:21 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-10-31 15:06:43 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-10-31 15:05:24 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-10-31 16:01:24 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-31 15:03:13 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-10-31 15:02:19 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-10-31 15:02:30 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-10-31 15:00:21 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.023 |  |
| 2026-10-31 15:12:54 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | -0.029 |  |
| 2026-10-31 15:05:56 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-10-31 15:05:10 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | -0.033 |  |
| 2026-10-31 15:10:54 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.035 |  |
| 2026-10-31 15:13:12 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.035 |  |
| 2026-10-31 15:02:20 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.040 |  |
| 2026-10-31 15:02:31 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.080 |  |
| 2026-10-31 16:02:52 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.081 |  |
| 2026-10-31 15:07:04 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.102 |  |
| 2026-10-31 15:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)