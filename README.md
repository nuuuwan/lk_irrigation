# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_05:04:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,363 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 05:04:38 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-24 05:04:02 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.048 |  |
| 2026-10-24 05:03:47 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 05:03:34 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.020 |  |
| 2026-10-24 05:03:09 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | -0.030 |  |
| 2026-10-24 05:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | -7.448 |  |
| 2026-10-24 05:02:43 | Hanwella (Kelani Ganga) | 3.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 05:02:35 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-24 05:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -7.448 |  |
| 2026-10-24 05:02:16 | Moragaswewa (Deduru Oya) | 3.59 | 🟢 Normal | -0.111 |  |
| 2026-10-24 05:01:51 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-24 05:01:25 | Ellagawa (Kalu Ganga) | 6.61 | 🟢 Normal | -0.093 |  |
| 2026-10-24 05:01:11 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-24 05:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-24 05:01:02 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-10-24 05:00:42 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 04:31:01 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-10-24 04:22:49 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -36.000 |  |
| 2026-10-24 04:22:48 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -36.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 04:04:38 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-24 04:03:49 | Glencourse (Kelani Ganga) | 11.54 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-24 04:14:25 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-24 05:02:43 | Hanwella (Kelani Ganga) | 3.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 02:01:16 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 05:00:42 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-24 05:01:51 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-24 05:04:38 | Giriulla (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-24 04:10:56 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-24 04:31:01 | Panadugama (Nilwala Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-10-24 04:02:11 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-24 04:05:44 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-24 05:03:47 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 04:11:34 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-24 02:10:02 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.005 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-24 05:01:11 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-24 05:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-24 04:01:08 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-10-24 05:02:35 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-24 05:03:34 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.020 |  |
| 2026-10-24 04:06:09 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-10-24 04:02:45 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-24 00:04:07 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.021 |  |
| 2026-10-24 04:00:38 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.023 |  |
| 2026-10-24 05:03:09 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | -0.030 |  |
| 2026-10-24 05:01:02 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-10-24 04:02:54 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-10-24 04:11:59 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.038 |  |
| 2026-10-24 04:01:48 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.038 |  |
| 2026-10-24 04:12:00 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.040 |  |
| 2026-10-24 05:04:02 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.048 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-24 05:01:25 | Ellagawa (Kalu Ganga) | 6.61 | 🟢 Normal | -0.093 |  |
| 2026-10-24 05:02:16 | Moragaswewa (Deduru Oya) | 3.59 | 🟢 Normal | -0.111 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |
| 2026-10-24 05:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | -7.448 |  |
| 2026-10-24 04:22:49 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)