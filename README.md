# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_08:06:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,591 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 08:06:01 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:05:55 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.020 |  |
| 2026-02-05 08:05:48 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.023 |  |
| 2026-02-05 08:04:54 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:04:44 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.098 |  |
| 2026-02-05 08:04:40 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:04:34 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:04:33 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-05 08:04:21 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-02-05 08:03:58 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:03:49 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-02-05 08:03:42 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.118 |  |
| 2026-02-05 08:03:33 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 08:03:07 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:03:00 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.082 |  |
| 2026-02-05 08:02:53 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:02:45 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:02:41 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:02:38 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 08:02:36 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 08:02:02 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:01:52 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:00:52 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.030 |  |
| 2026-02-05 08:00:52 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-05 08:00:45 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 07:56:21 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-05 07:41:20 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-05 07:32:01 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-05 07:28:52 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 07:19:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 07:18:03 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-05 07:12:43 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.023 |  |
| 2026-02-05 07:11:48 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.082 |  |
| 2026-02-05 07:11:12 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 07:18:03 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-05 06:07:34 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-05 08:02:36 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 08:03:33 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 08:02:38 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 08:02:02 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:03:07 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:02:45 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:02:41 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:04:40 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-05 07:56:21 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:03:58 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:00:45 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:02:53 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:04:34 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:01:52 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 07:06:58 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:04:54 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-05 08:06:01 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 07:11:12 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-05 08:04:21 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-02-05 08:04:33 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-05 08:03:49 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-02-05 08:00:52 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-05 08:05:55 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-05 08:05:48 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.023 |  |
| 2026-02-05 07:01:05 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.030 |  |
| 2026-02-05 08:00:52 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.030 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-05 08:03:00 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.082 |  |
| 2026-02-05 08:04:44 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.098 |  |
| 2026-02-03 22:06:20⌛ | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |
| 2026-02-05 08:03:42 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)