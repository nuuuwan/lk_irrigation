# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_10:26:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,572 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 10:26:19 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:26:15 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:26:11 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:26:06 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:09:52 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:09:38 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:09:12 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-10-24 10:08:11 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 10:07:34 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.019 |  |
| 2026-10-24 10:06:55 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:06:14 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.019 |  |
| 2026-10-24 10:06:13 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:05:44 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-10-24 10:05:37 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 10:05:32 | Ellagawa (Kalu Ganga) | 6.37 | 🟢 Normal | -0.053 |  |
| 2026-10-24 10:05:26 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.029 |  |
| 2026-10-24 10:04:42 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.116 |  |
| 2026-10-24 10:04:06 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-10-24 10:03:43 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.049 |  |
| 2026-10-24 10:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.01 | 🟢 Normal | -0.030 |  |
| 2026-10-24 10:03:36 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.061 |  |
| 2026-10-24 10:03:19 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.029 |  |
| 2026-10-24 10:03:17 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.040 |  |
| 2026-10-24 10:03:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-24 10:02:59 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:02:34 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.029 |  |
| 2026-10-24 10:02:33 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:02:30 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-24 10:02:18 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.081 |  |
| 2026-10-24 10:02:14 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-24 10:02:04 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-10-24 10:02:02 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 10:01:53 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:01:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-24 10:01:36 | Moragaswewa (Deduru Oya) | 3.12 | 🟢 Normal | -0.107 |  |
| 2026-10-24 10:01:29 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:01:16 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:01:15 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:01:05 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-24 10:00:49 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:00:19 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.021 |  |
| 2026-10-24 10:00:17 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 10:04:06 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-10-24 10:01:05 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-24 10:01:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-24 10:02:02 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 10:08:11 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 10:05:37 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-24 10:02:59 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:02:33 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:01:16 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:09:38 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:06:13 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:01:29 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:09:52 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:00:49 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:26:19 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:06:55 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:01:15 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:01:53 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 10:09:12 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-10-24 10:03:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-24 10:02:30 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-24 10:02:14 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-24 10:07:34 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.019 |  |
| 2026-10-24 10:06:14 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | -0.019 |  |
| 2026-10-24 10:02:04 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-10-24 10:00:19 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.021 |  |
| 2026-10-24 10:05:26 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.029 |  |
| 2026-10-24 10:03:19 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.029 |  |
| 2026-10-24 10:02:34 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.029 |  |
| 2026-10-24 10:05:44 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-10-24 10:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.01 | 🟢 Normal | -0.030 |  |
| 2026-10-24 10:00:17 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.031 |  |
| 2026-10-24 10:03:17 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.040 |  |
| 2026-10-24 10:03:43 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.049 |  |
| 2026-10-24 10:05:32 | Ellagawa (Kalu Ganga) | 6.37 | 🟢 Normal | -0.053 |  |
| 2026-10-24 10:03:36 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.061 |  |
| 2026-10-24 10:02:18 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.081 |  |
| 2026-10-24 10:01:36 | Moragaswewa (Deduru Oya) | 3.12 | 🟢 Normal | -0.107 |  |
| 2026-10-24 10:04:42 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)