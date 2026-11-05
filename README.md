# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_01:03:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,963 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 01:03:09 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-06 01:03:05 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -28.315 |  |
| 2026-11-06 01:02:51 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 01:02:36 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 01:02:29 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:02:03 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | -0.088 |  |
| 2026-11-06 01:01:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:01:58 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:01:36 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -28.315 |  |
| 2026-11-06 01:01:15 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:00:45 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.020 |  |
| 2026-11-06 00:32:20 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.007 |  |
| 2026-11-06 00:29:31 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 01:03:09 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-06 00:05:30 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-06 00:03:19 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-06 01:02:51 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 00:02:44 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 00:03:08 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 01:02:36 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 00:00:13 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:09:57 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:01:31 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:01:25 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:12:21 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:02:29 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:06:47 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-05 23:06:17 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:01:58 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:03:59 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:00:26 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:01:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:05:18 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:03:14 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:01:46 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-11-06 01:01:15 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-06 00:32:20 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.007 |  |
| 2026-11-06 00:29:31 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.007 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-06 00:06:03 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-11-06 01:00:45 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.020 |  |
| 2026-11-06 00:07:26 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.040 |  |
| 2026-11-06 00:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | -0.040 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-06 00:04:12 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.049 |  |
| 2026-11-05 23:08:59 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | -0.064 |  |
| 2026-11-06 01:02:03 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | -0.088 |  |
| 2026-11-06 00:04:54 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.092 |  |
| 2026-11-06 00:12:57 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -18.000 |  |
| 2026-11-06 01:03:05 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -28.315 |  |
| 2026-11-06 00:05:57 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -218.805 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)