# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_12:13:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,267 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 12:13:05 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:11:49 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.088 |  |
| 2026-02-19 12:08:52 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:08:21 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:07:49 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:07:30 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:07:14 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:06:38 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:06:27 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.024 |  |
| 2026-02-19 12:05:47 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:05:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:05:12 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:04:37 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:04:33 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:04:10 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-19 12:04:00 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-19 12:03:41 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:03:28 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:03:23 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-19 12:03:10 | Manampitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.020 |  |
| 2026-02-19 12:02:54 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:02:53 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-19 12:02:48 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-02-19 12:02:46 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-02-19 12:02:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:02:40 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:02:37 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:02:28 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-19 12:02:22 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-02-19 12:02:12 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-19 12:02:11 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:01:54 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:01:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.054 |  |
| 2026-02-19 12:01:41 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:01:39 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.102 |  |
| 2026-02-19 12:01:24 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 12:01:22 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:01:06 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:00:11 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 12:02:48 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-02-19 12:02:28 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-19 12:01:24 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 12:04:10 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-19 12:02:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:02:40 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:02:54 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:01:41 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:05:12 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:06:38 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:03:41 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:07:49 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:07:14 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:01:06 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:03:28 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:02:22 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:13:05 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:04:33 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:02:11 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:04:37 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:08:21 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:02:37 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:05:47 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:01:22 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:08:52 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:01:54 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-19 12:03:23 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-19 12:04:00 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-19 12:02:12 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-02-19 12:00:11 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-19 12:02:53 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-02-19 12:03:10 | Manampitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.020 |  |
| 2026-02-19 12:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-02-19 12:02:46 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-02-19 12:06:27 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.024 |  |
| 2026-02-19 12:01:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.054 |  |
| 2026-02-19 12:11:49 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.088 |  |
| 2026-02-19 12:01:39 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)