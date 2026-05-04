# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_04:31:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,201 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 04:31:35 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.007 |  |
| 2026-05-05 04:29:23 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.004 |  |
| 2026-05-05 04:28:35 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-05 04:17:10 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-05 04:12:05 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 04:11:53 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.319 |  |
| 2026-05-05 04:11:17 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:11:09 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 5.268 | 🔺 Rising |
| 2026-05-05 04:10:28 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 5.268 | 🔺 Rising |
| 2026-05-05 04:08:56 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-05 04:08:33 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.117 |  |
| 2026-05-05 04:08:00 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-05-05 04:06:50 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:06:42 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-05 04:06:32 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:05:58 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.444 | 🔺 Rising |
| 2026-05-05 04:05:20 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-05-05 04:05:18 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:05:03 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:04:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 04:04:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-05 04:03:41 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:03:18 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-05-05 04:03:11 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:02:38 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:02:17 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-05-05 04:02:04 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:02:03 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.101 |  |
| 2026-05-05 04:01:40 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-05-05 04:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:01:12 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:00:53 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.042 |  |
| 2026-05-05 04:00:25 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.074 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 04:11:09 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 5.268 | 🔺 Rising |
| 2026-05-05 04:05:58 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.444 | 🔺 Rising |
| 2026-05-05 04:05:20 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-05-05 01:20:45 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-05 01:16:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-05 04:04:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-05 04:08:56 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-05 04:17:10 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-05 04:06:42 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-05 04:28:35 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-05 04:12:05 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 04:04:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:02:04 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:06:50 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:01:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:01:12 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:05:18 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:06:32 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:11:17 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:02:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:05:03 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:03:41 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:02:38 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-05 03:08:27 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 04:29:23 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.004 |  |
| 2026-05-05 04:31:35 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.007 |  |
| 2026-05-05 04:08:00 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-05-05 04:02:17 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-05-05 04:03:18 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-05-05 04:01:40 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-05-05 04:00:53 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.042 |  |
| 2026-05-05 03:05:50 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.061 |  |
| 2026-05-05 04:00:25 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.074 |  |
| 2026-05-05 04:02:03 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.101 |  |
| 2026-05-05 04:08:33 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.117 |  |
| 2026-05-05 04:11:53 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.319 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)