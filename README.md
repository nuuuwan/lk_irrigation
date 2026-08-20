# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_05:22:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,303 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 05:22:29 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:18:49 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-20 05:17:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:17:01 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-20 05:16:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-20 05:11:37 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-20 05:11:08 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:10:49 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-08-20 05:09:52 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-20 05:09:24 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 05:05:41 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-08-20 05:02:46 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-08-20 05:10:49 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-08-20 05:00:53 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-08-20 05:02:15 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-20 05:03:59 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-20 05:04:58 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-20 05:04:57 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-20 05:16:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-20 05:08:13 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-20 05:01:49 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-20 05:09:52 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-20 03:02:06 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-20 05:01:57 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 05:09:24 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-20 05:17:01 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-20 05:05:18 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 05:18:49 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-20 04:19:18 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-20 05:02:34 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:00:52 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:02:35 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:01:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:02:30 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:03:15 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-19 18:02:52 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:17:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 04:03:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:00:54 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:01:49 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:22:29 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:01:49 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-19 18:02:30 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:11:08 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 05:11:37 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-20 05:03:07 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-08-19 18:01:56 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-08-20 05:07:53 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.031 |  |
| 2026-08-20 05:04:21 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)