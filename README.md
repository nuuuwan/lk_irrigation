# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_08:03:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,762 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 08:03:49 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:03:47 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:03:39 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-01 08:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.061 |  |
| 2026-10-01 08:03:25 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-10-01 08:02:47 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:46 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:20 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:14 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.033 |  |
| 2026-10-01 08:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-10-01 08:02:02 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:01:54 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.070 |  |
| 2026-10-01 08:01:05 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:00:44 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-10-01 08:00:43 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-10-01 08:00:28 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 07:05:57 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-01 07:03:07 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-01 07:05:47 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-01 07:04:31 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 08:01:05 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-01 07:01:33 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 07:04:56 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 06:06:36 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:46 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-01 07:04:10 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:20 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:05:54 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 07:03:40 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:03:47 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:47 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 07:08:52 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:03:49 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-01 07:08:32 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 07:04:41 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-01 07:10:31 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-01 07:13:35 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:02 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 07:20:38 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.008 |  |
| 2026-10-01 07:06:12 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.009 |  |
| 2026-10-01 08:03:39 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-01 08:00:43 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-10-01 07:04:14 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-01 08:00:28 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-01 08:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-10-01 07:09:25 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.018 |  |
| 2026-10-01 08:03:25 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-10-01 07:05:25 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.023 |  |
| 2026-10-01 08:02:14 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.033 |  |
| 2026-10-01 08:00:44 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-10-01 08:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.061 |  |
| 2026-10-01 08:01:54 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.070 |  |
| 2026-10-01 07:04:29 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.076 |  |
| 2026-10-01 07:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.097 |  |
| 2026-10-01 07:00:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)