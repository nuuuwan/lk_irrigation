# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_02:41:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,256 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 02:41:39 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-10 02:14:44 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:12:08 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-10 02:10:41 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:08:58 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-08-10 02:07:28 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-08-10 02:07:12 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-10 02:06:55 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-08-10 02:06:42 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 02:06:32 | Kithulgala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 02:06:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-08-10 02:06:08 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.019 |  |
| 2026-08-10 02:05:09 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:05:05 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.059 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 02:07:28 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 3.273 | 🔺 Rising |
| 2026-08-10 00:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-10 02:02:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-10 02:06:32 | Kithulgala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 02:01:48 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 01:24:25 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-10 02:06:42 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 02:41:39 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 02:03:47 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 02:07:12 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-10 02:10:41 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:42:15 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:01:19 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:02:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:02:43 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:30:34 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:02:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:01:26 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:01:38 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:03:35 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:14:44 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:02:32 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:01:11 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:02:06 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:05:09 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-10 02:03:39 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-08-10 02:12:08 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-10 02:06:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-08-10 02:02:44 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-08-10 02:08:58 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-08-10 02:02:15 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-08-10 01:04:26 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.012 |  |
| 2026-08-10 02:06:08 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.019 |  |
| 2026-08-10 02:01:36 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | -0.030 |  |
| 2026-08-10 02:04:51 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.039 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-10 02:05:05 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)