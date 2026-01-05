# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_08:21:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,132 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 08:21:22 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:17:18 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -2.000 |  |
| 2026-01-05 08:17:00 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -2.000 |  |
| 2026-01-05 08:16:04 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-05 08:13:03 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -0.008 |  |
| 2026-01-05 08:13:00 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-05 08:11:39 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-01-05 08:07:51 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-05 08:06:33 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.022 |  |
| 2026-01-05 08:05:36 | Galgamuwa (Mee Oya) | 1.19 | 🟢 Normal | -0.007 |  |
| 2026-01-05 08:05:34 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-01-05 08:05:22 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.090 |  |
| 2026-01-05 08:05:16 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-01-05 08:05:08 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:05:06 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.012 |  |
| 2026-01-05 08:05:02 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-05 08:04:54 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:04:52 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 08:04:16 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 08:04:05 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.055 |  |
| 2026-01-05 08:03:56 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:03:30 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-05 08:03:27 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:03:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.154 |  |
| 2026-01-05 08:03:17 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.050 |  |
| 2026-01-05 08:03:06 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 08:03:05 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:02:42 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:02:39 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:02:38 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.080 |  |
| 2026-01-05 08:02:25 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:02:14 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:01:36 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-01-05 08:01:23 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-01-05 08:01:20 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 08:01:14 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-05 08:01:08 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.014 |  |
| 2026-01-05 08:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:00:43 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 08:05:34 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-01-05 08:01:14 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-05 08:05:02 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-05 08:07:51 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-05 08:04:16 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 08:16:04 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-05 08:00:43 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 08:03:06 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 08:01:20 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 08:04:52 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 08:02:14 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:02:42 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:03:05 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:05:08 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:02:38 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:03:56 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:03:27 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:02:25 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:21:22 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:04:54 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:02:39 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:05:36 | Galgamuwa (Mee Oya) | 1.19 | 🟢 Normal | -0.007 |  |
| 2026-01-05 08:13:03 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | -0.008 |  |
| 2026-01-05 08:11:39 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-01-05 08:05:16 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-01-05 08:01:23 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-01-05 08:03:30 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-05 08:01:36 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-01-05 08:13:00 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-05 08:05:06 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.012 |  |
| 2026-01-05 08:01:08 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.014 |  |
| 2026-01-05 08:06:33 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.022 |  |
| 2026-01-05 08:03:17 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.050 |  |
| 2026-01-05 08:04:05 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.055 |  |
| 2026-01-05 08:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.080 |  |
| 2026-01-05 08:05:22 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.090 |  |
| 2026-01-05 08:03:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.154 |  |
| 2026-01-05 08:17:18 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -2.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)