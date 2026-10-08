# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_07:48:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,052 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 07:48:05 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.006 |  |
| 2026-10-08 07:18:00 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-08 07:13:56 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.051 |  |
| 2026-10-08 07:13:37 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.018 |  |
| 2026-10-08 07:09:44 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:09:10 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-08 07:08:05 | Dunamale (Aththanagalu Oya) | 2.97 | 🟢 Normal | -0.019 |  |
| 2026-10-08 07:08:00 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.072 |  |
| 2026-10-08 07:07:52 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.091 |  |
| 2026-10-08 07:07:40 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.090 |  |
| 2026-10-08 07:07:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.001 |  |
| 2026-10-08 07:07:02 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 07:05:33 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-10-08 07:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-10-08 07:02:10 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-10-08 07:18:00 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-08 07:02:28 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 07:09:10 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-08 07:04:16 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 07:07:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.001 |  |
| 2026-10-08 07:09:44 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:03:20 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:00:35 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:01:33 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:01:07 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:03:22 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:05:45 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:04:17 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:05:28 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:03:37 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:05:09 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:02:51 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-08 07:48:05 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.006 |  |
| 2026-10-08 07:07:02 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-08 07:13:37 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.018 |  |
| 2026-10-08 07:08:05 | Dunamale (Aththanagalu Oya) | 2.97 | 🟢 Normal | -0.019 |  |
| 2026-10-08 06:01:59 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-10-08 07:02:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-10-08 07:01:03 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-10-08 07:04:07 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.039 |  |
| 2026-10-08 07:13:56 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.051 |  |
| 2026-10-08 07:00:57 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.053 |  |
| 2026-10-08 07:03:32 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.059 |  |
| 2026-10-08 07:04:15 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.066 |  |
| 2026-10-08 07:08:00 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.072 |  |
| 2026-10-08 07:04:48 | Nagalagam Street (Kelani Ganga) | 0.38 | 🟢 Normal | -0.080 |  |
| 2026-10-08 07:04:18 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.085 |  |
| 2026-10-08 07:02:52 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.090 |  |
| 2026-10-08 07:07:40 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.090 |  |
| 2026-10-08 07:07:52 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.091 |  |
| 2026-10-08 07:05:03 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | -0.184 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)