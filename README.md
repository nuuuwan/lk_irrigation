# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_20:19:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,944 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 20:19:25 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:14:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.025 |  |
| 2026-04-25 20:14:10 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.014 |  |
| 2026-04-25 20:13:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-25 20:10:08 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-04-25 20:08:33 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-04-25 20:07:53 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 20:07:46 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.057 |  |
| 2026-04-25 20:07:16 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:06:26 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.022 |  |
| 2026-04-25 20:06:26 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:05:32 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:05:11 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:04:14 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:04:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:04:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:03:35 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-25 20:03:26 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:03:21 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.060 |  |
| 2026-04-25 20:03:18 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-04-25 20:03:13 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-25 20:03:11 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-25 20:02:49 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-25 20:02:25 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-25 20:02:23 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:02:15 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-04-25 20:02:12 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:02:06 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.059 |  |
| 2026-04-25 20:01:56 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:01:49 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.022 |  |
| 2026-04-25 20:01:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:01:40 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-25 20:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-04-25 20:01:11 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-25 20:01:09 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:00:23 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 20:02:49 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-25 20:01:11 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-25 20:03:11 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-25 20:01:40 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-25 20:07:53 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 20:07:16 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:02:23 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:05:32 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:01:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:01:56 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:03:26 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:04:14 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:04:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:00:23 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:04:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:02:12 | Katharagama (Menik Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:05:11 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:06:26 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:19:25 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:01:09 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 20:10:08 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-04-25 20:13:33 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-25 20:03:35 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-25 20:03:18 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-04-25 20:02:25 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-25 20:03:13 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-25 20:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-04-25 20:14:10 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.014 |  |
| 2026-04-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 20:08:33 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-04-25 18:01:09 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-04-25 20:06:26 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.022 |  |
| 2026-04-25 20:01:49 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.022 |  |
| 2026-04-25 20:14:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.025 |  |
| 2026-04-25 20:02:15 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-04-25 18:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-04-25 20:07:46 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.057 |  |
| 2026-04-25 20:02:06 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.059 |  |
| 2026-04-25 20:03:21 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)