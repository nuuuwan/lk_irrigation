# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_09:10:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,933 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 09:10:00 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.022 |  |
| 2026-02-21 09:06:57 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:06:52 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.097 |  |
| 2026-02-21 09:06:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.140 |  |
| 2026-02-21 09:06:03 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-02-21 09:05:56 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:05:24 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:05:22 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:05:15 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 09:04:56 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-02-21 09:04:33 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 09:04:29 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-21 09:04:27 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.014 |  |
| 2026-02-21 09:04:17 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:04:09 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.061 |  |
| 2026-02-21 09:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | -0.086 |  |
| 2026-02-21 09:03:46 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-21 09:03:39 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.049 |  |
| 2026-02-21 09:03:28 | Manampitiya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.029 |  |
| 2026-02-21 09:03:27 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:03:24 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:03:10 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:03:01 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-02-21 09:02:56 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 09:02:53 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:02:43 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-21 09:02:36 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-02-21 09:02:22 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-02-21 09:02:09 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-02-21 09:01:49 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-21 09:01:43 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-21 09:01:43 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-02-21 09:01:34 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:01:33 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:57 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 09:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:46 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:06 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 09:02:22 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-02-21 09:04:56 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-02-21 09:03:46 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-21 09:01:43 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-21 09:02:56 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 09:00:57 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 09:05:15 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 09:04:33 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 09:03:10 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:01:34 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:06:57 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:03:24 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:05:56 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:03:27 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:05:24 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:06 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:05:22 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:02:53 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:01:33 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:00:46 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 09:04:29 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-02-21 09:02:36 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-02-21 09:03:01 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-02-21 09:01:49 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-21 09:02:43 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-02-21 09:01:43 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-02-21 09:06:03 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.011 |  |
| 2026-02-21 09:04:27 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.014 |  |
| 2026-02-21 09:02:09 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-02-21 09:10:00 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.022 |  |
| 2026-02-21 09:03:28 | Manampitiya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.029 |  |
| 2026-02-21 08:09:43 | Padiyathalawa (Maduru Oya) | 1.62 | 🟢 Normal | -0.036 |  |
| 2026-02-21 09:03:39 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.049 |  |
| 2026-02-21 09:04:09 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.061 |  |
| 2026-02-21 09:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | -0.086 |  |
| 2026-02-21 09:06:52 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.097 |  |
| 2026-02-21 09:06:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.140 |  |
| 2026-02-21 08:04:52 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -38.400 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)