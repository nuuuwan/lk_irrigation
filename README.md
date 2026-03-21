# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_18:10:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,609 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 18:10:21 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:09:56 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:07:12 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-03-21 18:06:45 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.057 |  |
| 2026-03-21 18:06:23 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:06:18 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:04:57 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:04:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.097 |  |
| 2026-03-21 18:03:54 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:03:31 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:03:23 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-03-21 18:03:22 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-21 18:03:21 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:02:43 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-03-21 18:02:41 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-03-21 18:02:37 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:02:37 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 18:02:16 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-21 18:02:06 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:54 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:51 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-03-21 18:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:35 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:34 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-21 18:01:31 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-21 18:01:17 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:16 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:15 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-03-21 18:01:07 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:02 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:00:48 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:00:38 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:00:19 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.082 |  |
| 2026-03-21 18:00:17 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:00:15 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-03-21 18:00:14 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.067 |  |
| 2026-03-21 18:00:12 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 18:07:12 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-03-21 18:02:43 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-03-21 18:02:41 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-03-21 18:01:31 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-21 18:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-21 18:03:22 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-21 18:01:34 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-21 18:02:37 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 18:01:16 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:00:48 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:09:56 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-21 17:01:46 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:02:16 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:00:38 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:02 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:17 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:02:06 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:02:37 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:00:17 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:03:54 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:06:23 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:04:57 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:10:21 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:06:18 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:54 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:03:21 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:03:31 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:07 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:35 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:00:15 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-03-21 18:00:12 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-03-21 18:01:51 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-03-21 18:03:23 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-03-21 18:01:15 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-03-21 18:06:45 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.057 |  |
| 2026-03-21 18:00:14 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.067 |  |
| 2026-03-21 18:00:19 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.082 |  |
| 2026-03-21 18:04:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)