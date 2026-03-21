# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_02:22:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 02:22:50 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:15:01 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-03-22 02:15:00 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-03-22 02:12:16 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:11:43 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-22 02:10:50 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:09:31 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-22 02:07:01 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.031 |  |
| 2026-03-22 02:04:57 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:04:30 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 5.714 | 🔺 Rising |
| 2026-03-22 02:04:20 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-22 02:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-03-22 02:04:17 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-03-22 02:04:09 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:03:54 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.004 |  |
| 2026-03-22 02:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-03-22 02:03:28 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.032 |  |
| 2026-03-22 02:03:26 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:03:26 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.040 |  |
| 2026-03-22 02:03:16 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-03-22 02:02:58 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:02:56 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:02:48 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-03-22 02:02:27 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-03-22 02:02:25 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:02:24 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 5.714 | 🔺 Rising |
| 2026-03-22 02:02:23 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-03-22 02:02:09 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-22 02:02:07 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-03-22 02:02:01 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:01:31 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-22 02:01:29 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 02:00:54 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-03-22 02:00:39 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 02:15:01 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-03-22 02:04:30 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 5.714 | 🔺 Rising |
| 2026-03-22 02:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 5.000 | 🔺 Rising |
| 2026-03-22 02:09:31 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-22 02:01:31 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-22 02:02:09 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-22 02:04:20 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-22 02:01:29 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 02:03:54 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.004 |  |
| 2026-03-22 02:03:26 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:00:39 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:02:25 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:08:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:02:56 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:22:50 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:02 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:12:16 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:10:50 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:02:58 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:02:01 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:04:09 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:04:57 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-22 00:00:48 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 02:03:16 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-22 01:10:15 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-03-22 02:11:43 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-22 02:02:27 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-03-22 02:02:07 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-03-22 02:02:23 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:35 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-03-22 02:02:48 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-03-22 02:04:17 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-03-22 02:07:01 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.031 |  |
| 2026-03-22 02:03:28 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.032 |  |
| 2026-03-22 02:03:26 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.040 |  |
| 2026-03-22 02:00:54 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-03-21 18:00:19 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.082 |  |
| 2026-03-21 22:04:33 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)