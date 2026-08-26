# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_08:00:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,743 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **2** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 08:00:42 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:31:01 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 07:02:25 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-08-26 07:05:37 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-26 07:05:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-26 07:07:08 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-26 07:03:52 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-26 07:15:12 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-26 07:31:01 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-26 07:04:59 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-26 07:15:23 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-26 07:06:51 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 07:09:20 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 07:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 07:03:16 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 07:04:09 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 07:06:09 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-26 07:12:02 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-26 07:02:42 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:01:54 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:00:46 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:02:10 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:05:07 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:00:55 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:04:02 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:00:14 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:02:59 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:01:03 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:03:01 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:00:42 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:06:01 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:04:14 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:01:53 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:02:07 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-26 07:02:31 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | -0.002 |  |
| 2026-08-26 07:07:09 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-08-26 07:08:06 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.019 |  |
| 2026-08-26 07:01:26 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.041 |  |
| 2026-08-26 07:04:58 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.087 |  |
| 2026-08-26 07:08:20 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.229 |  |
| 2026-08-26 07:02:31 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -7.200 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)