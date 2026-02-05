# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_09:17:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,629 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 09:17:28 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:11:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.044 |  |
| 2026-02-05 09:09:44 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:07:04 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:06:24 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-05 09:06:23 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.020 |  |
| 2026-02-05 09:05:55 | Dunamale (Aththanagalu Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-02-05 09:05:02 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:04:40 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:04:27 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.120 |  |
| 2026-02-05 09:03:47 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:03:47 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-02-05 09:03:32 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:03:30 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-05 09:03:30 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-05 09:03:27 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:03:17 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:03:09 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-02-05 09:03:07 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:03:04 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:03:02 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-05 09:02:41 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:02:12 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:02:08 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:02:07 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:02:01 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-02-05 09:01:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:01:41 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-05 09:01:38 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.045 |  |
| 2026-02-05 09:01:37 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-05 09:00:45 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:00:22 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.071 |  |
| 2026-02-05 09:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 06:07:34 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-05 09:03:02 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-05 09:03:30 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-05 09:01:41 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-05 09:01:37 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-05 09:03:04 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:01:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:02:41 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:17:28 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:00:45 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:07:04 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:03:32 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:03:47 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:04:40 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:03:07 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:02:07 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:02:08 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:05:02 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:03:27 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 09:09:44 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-05 09:05:55 | Dunamale (Aththanagalu Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-02-05 09:06:24 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-05 09:03:30 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-02-05 09:03:09 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-02-05 09:02:01 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-02-05 09:06:23 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-05 09:03:47 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-02-05 09:11:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.044 |  |
| 2026-02-05 09:01:38 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.045 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-05 09:00:22 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.071 |  |
| 2026-02-03 22:06:20⌛ | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |
| 2026-02-05 09:04:27 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)