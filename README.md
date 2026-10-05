# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_03:08:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 03:08:13 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-10-06 03:07:07 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-06 03:06:57 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-10-06 03:06:19 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:06:07 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-10-06 03:05:32 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-06 03:04:38 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.048 |  |
| 2026-10-06 03:04:26 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.035 |  |
| 2026-10-06 03:04:15 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-06 03:03:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:03:38 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-06 03:03:35 | Glencourse (Kelani Ganga) | 12.73 | 🟢 Normal | -0.257 |  |
| 2026-10-06 03:03:33 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-06 03:03:32 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-06 03:03:27 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.110 |  |
| 2026-10-06 03:02:59 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 03:02:51 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.208 |  |
| 2026-10-06 03:02:34 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-10-06 03:02:09 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-10-06 03:01:00 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 03:00:33 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:00:22 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.050 |  |
| 2026-10-06 03:00:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:29:03 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.118 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 01:08:47 | Hanwella (Kelani Ganga) | 4.24 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-10-06 03:05:32 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-06 03:06:57 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-10-06 02:29:03 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-06 03:04:15 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-06 03:07:07 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-06 02:16:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-06 03:03:33 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-06 03:02:59 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 02:20:02 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-06 03:01:00 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 03:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:00:33 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:02:09 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:00:21 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:02:30 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:03:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 02:24:03 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:06:19 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-06 03:08:13 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-10-06 03:03:32 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-06 01:05:47 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-06 03:03:38 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-06 03:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-10-06 03:02:34 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-10-06 01:03:14 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2026-10-06 03:06:07 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-10-06 03:04:26 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.035 |  |
| 2026-10-06 02:13:23 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.043 |  |
| 2026-10-06 03:04:38 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.048 |  |
| 2026-10-05 22:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.048 |  |
| 2026-10-06 03:00:22 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.050 |  |
| 2026-10-06 02:08:09 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.098 |  |
| 2026-10-06 03:03:27 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.110 |  |
| 2026-10-06 03:02:51 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.208 |  |
| 2026-10-06 03:03:35 | Glencourse (Kelani Ganga) | 12.73 | 🟢 Normal | -0.257 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)