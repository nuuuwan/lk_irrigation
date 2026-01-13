# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_18:27:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,686 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 18:27:05 | Horowpothana (Yan Oya) | 3.93 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-13 18:25:42 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:10:28 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-13 18:10:09 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.012 |  |
| 2026-01-13 18:08:56 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.009 |  |
| 2026-01-13 18:08:43 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-13 18:08:06 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:07:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-01-13 18:06:15 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-13 18:05:52 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:04:39 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 18:04:31 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:04:12 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:04:02 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 18:03:54 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:35 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-01-13 18:03:30 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:23 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-13 18:03:03 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:02:54 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.091 |  |
| 2026-01-13 18:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-01-13 18:02:36 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | -0.024 |  |
| 2026-01-13 18:02:31 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:02:30 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.025 |  |
| 2026-01-13 18:02:28 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-01-13 18:02:28 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:02:27 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:02:09 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.037 |  |
| 2026-01-13 18:02:01 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:01:36 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:01:33 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:01:30 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:01:30 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-13 18:01:22 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.022 |  |
| 2026-01-13 18:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 18:01:20 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:01:14 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.040 |  |
| 2026-01-13 18:01:11 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-13 18:00:48 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 18:01:30 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-13 18:08:43 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-13 18:10:28 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-13 18:01:11 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-13 18:06:15 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-13 18:04:02 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 18:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 18:04:39 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 18:27:05 | Horowpothana (Yan Oya) | 3.93 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-13 18:02:01 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:00:48 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:04:12 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:54 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:30 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:01:33 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:08:06 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:05:52 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:02:31 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:23 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:25:42 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:01:30 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:08:56 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.009 |  |
| 2026-01-13 18:02:28 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:02:27 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:01:36 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:04:31 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:01:20 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:02:28 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-01-13 18:10:09 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.012 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-13 18:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-01-13 18:03:35 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-01-13 18:01:22 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.022 |  |
| 2026-01-13 18:02:36 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | -0.024 |  |
| 2026-01-13 18:02:30 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.025 |  |
| 2026-01-13 18:07:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-01-13 18:02:09 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.037 |  |
| 2026-01-13 18:01:14 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.040 |  |
| 2026-01-13 18:02:54 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)