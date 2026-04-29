# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_14:35:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,272 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 14:35:28 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.042 |  |
| 2026-04-29 14:29:01 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.007 |  |
| 2026-04-29 14:16:51 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.044 |  |
| 2026-04-29 14:10:20 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-04-29 14:08:50 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-04-29 14:08:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-04-29 14:08:33 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.028 |  |
| 2026-04-29 14:07:33 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:07:19 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:06:55 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:04:52 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-04-29 14:04:43 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-29 14:04:43 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.057 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 14:02:43 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-29 14:01:49 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-29 14:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-29 14:02:10 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-29 14:04:43 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-29 14:02:15 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 14:03:33 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 13:08:34 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-29 14:01:35 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:02:10 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:00:38 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:02:25 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:02:32 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:02:58 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:04:05 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:07:33 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:07:19 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:03:54 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:01:36 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:04:00 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:06:55 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:00:30 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:29:01 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.007 |  |
| 2026-04-29 14:08:50 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-04-29 14:04:52 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-04-29 14:03:25 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-29 14:10:20 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-04-29 14:01:04 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-29 14:04:17 | Badalgama (Maha Oya) | 2.49 | 🟢 Normal | -0.011 |  |
| 2026-04-29 14:02:16 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.012 |  |
| 2026-04-29 14:02:39 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.020 |  |
| 2026-04-29 14:08:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-04-29 14:03:08 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-04-29 14:08:33 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.028 |  |
| 2026-04-29 14:00:48 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.036 |  |
| 2026-04-29 14:35:28 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.042 |  |
| 2026-04-29 14:16:51 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.044 |  |
| 2026-04-29 14:04:43 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.057 |  |
| 2026-04-29 14:03:22 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)