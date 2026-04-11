# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_06:21:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,907 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 06:21:41 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:09:37 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-11 06:09:29 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-04-11 06:08:09 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:06:30 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:06:07 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:05:45 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-11 06:05:40 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:05:26 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.048 |  |
| 2026-04-11 06:05:22 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-11 06:05:15 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.035 |  |
| 2026-04-11 06:05:14 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:05:10 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-04-11 06:04:57 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 06:04:27 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:03:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.034 |  |
| 2026-04-11 06:03:47 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 06:03:07 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-11 06:02:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:02:28 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-11 06:02:21 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.073 |  |
| 2026-04-11 06:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-04-11 06:02:11 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:02:06 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-04-11 06:02:03 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.039 |  |
| 2026-04-11 06:01:26 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-04-11 06:01:18 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:01:13 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.006 |  |
| 2026-04-11 06:01:13 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-04-11 06:01:11 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-11 06:01:07 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.090 |  |
| 2026-04-11 06:01:02 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.057 |  |
| 2026-04-11 06:00:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:00:22 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-11 06:00:14 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:43:43 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.224 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 06:01:13 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-04-11 05:08:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-04-11 06:05:10 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-04-11 06:02:06 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-04-11 06:02:28 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-11 06:09:37 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-11 06:03:07 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-11 06:05:22 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-11 06:04:57 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 06:03:47 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-11 06:00:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:00:14 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:02:35 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 05:01:08 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:06:07 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:21:41 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:05:14 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:08:09 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:05:40 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:01:18 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:02:11 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:04:27 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:06:30 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-11 06:01:13 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.006 |  |
| 2026-04-11 06:05:45 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-11 06:01:11 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-04-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-11 06:00:22 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-11 06:01:26 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-04-11 06:09:29 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-04-11 06:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-04-11 06:03:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.034 |  |
| 2026-04-11 06:05:15 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.035 |  |
| 2026-04-11 06:02:03 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.039 |  |
| 2026-04-11 06:05:26 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.048 |  |
| 2026-04-11 06:01:02 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.057 |  |
| 2026-04-11 05:06:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-04-11 06:02:21 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.073 |  |
| 2026-04-11 06:01:07 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)