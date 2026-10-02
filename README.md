# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_00:10:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,292 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 00:10:42 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:10:30 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-03 00:10:30 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-03 00:08:34 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-03 00:06:28 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 00:05:48 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-10-03 00:05:25 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-03 00:05:19 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:04:51 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:04:42 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.029 |  |
| 2026-10-03 00:04:26 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-03 00:04:11 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:03:31 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | -2.028 |  |
| 2026-10-03 00:03:25 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | -0.068 |  |
| 2026-10-03 00:03:23 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:03:00 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 00:02:58 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-03 00:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-10-03 00:02:49 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-10-03 00:02:46 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:02:44 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-10-03 00:02:39 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 00:02:23 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:02:20 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -2.028 |  |
| 2026-10-03 00:02:19 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -2.028 |  |
| 2026-10-03 00:02:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.011 |  |
| 2026-10-03 00:01:40 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-03 00:01:33 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:01:30 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:01:13 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-03 00:01:13 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-10-03 00:01:11 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 00:01:13 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-10-03 00:02:44 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-10-03 00:02:58 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-03 00:04:26 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-03 00:10:30 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-03 00:01:40 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-03 00:10:30 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-02 23:17:53 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-03 00:03:00 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 00:02:39 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 00:06:28 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 00:01:33 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:03:23 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:01:30 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:02:46 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:08:06 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:23:14 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:01:11 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:04:51 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:10:42 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:02:23 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:04:11 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:06:13 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:04:34 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:05:19 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:05:25 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-02 23:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-10-03 00:08:34 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-03 00:01:13 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-03 00:02:49 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-10-03 00:02:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.011 |  |
| 2026-10-03 00:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-10-03 00:04:42 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.029 |  |
| 2026-10-03 00:05:48 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-10-02 23:06:57 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.044 |  |
| 2026-10-03 00:03:25 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | -0.068 |  |
| 2026-10-02 23:11:36 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | -0.125 |  |
| 2026-10-03 00:03:31 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | -2.028 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)