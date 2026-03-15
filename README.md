# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_03:19:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,554 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 03:19:38 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-16 03:14:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-16 03:13:22 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:11:48 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:10:54 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.036 |  |
| 2026-03-16 03:08:20 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -108.000 |  |
| 2026-03-16 03:08:19 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -108.000 |  |
| 2026-03-16 03:07:50 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:07:38 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:07:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:06:08 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-03-16 03:05:47 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:05:16 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-16 03:04:57 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.058 |  |
| 2026-03-16 03:04:40 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-03-16 03:04:39 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.188 |  |
| 2026-03-16 03:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 1.662 | 🔺 Rising |
| 2026-03-16 03:03:55 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:03:24 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:03:05 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 03:02:47 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 03:02:46 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:02:40 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:02:13 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-16 03:02:10 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:02:08 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 1.662 | 🔺 Rising |
| 2026-03-16 03:01:45 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:01:39 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:01:25 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | -0.105 |  |
| 2026-03-16 03:01:12 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:01:05 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-16 03:00:56 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:00:21 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-16 02:49:57 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | -0.105 |  |
| 2026-03-16 02:49:29 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | -0.105 |  |
| 2026-03-16 02:42:37 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.053 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 03:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 1.662 | 🔺 Rising |
| 2026-03-16 03:05:16 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-16 03:00:21 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-16 03:02:13 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-16 03:19:38 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-16 03:14:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-16 03:01:05 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-16 03:02:47 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 03:03:05 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 03:07:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:01:39 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-16 01:00:48 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 02:03:55 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:01:45 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:11:48 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:13:22 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:07:38 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:02:08 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 02:02:42 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:02:40 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:05:47 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:03:24 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:07:50 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 03:02:46 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:02:10 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:03:55 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:00:56 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:01:12 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-03-16 03:06:08 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-03-16 03:04:40 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-03-16 03:10:54 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.036 |  |
| 2026-03-15 18:02:59 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.040 |  |
| 2026-03-16 03:04:57 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.058 |  |
| 2026-03-16 03:01:25 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | -0.105 |  |
| 2026-03-16 03:04:39 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.188 |  |
| 2026-03-16 03:08:20 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)