# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_08:05:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,613 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 08:05:18 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-03-17 08:05:12 | Nagalagam Street (Kelani Ganga) | 0.17 | 🟢 Normal | -0.031 |  |
| 2026-03-17 08:05:04 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:04:36 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 08:04:15 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-17 08:04:14 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-03-17 08:04:06 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-17 08:04:00 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.020 |  |
| 2026-03-17 08:03:34 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-03-17 08:03:19 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:03:18 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:03:17 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-17 08:03:17 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:03:00 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-17 08:02:43 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:02:16 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:02:15 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.081 |  |
| 2026-03-17 08:02:02 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.194 |  |
| 2026-03-17 08:01:58 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.073 |  |
| 2026-03-17 08:01:53 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:01:48 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-03-17 08:01:24 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.014 |  |
| 2026-03-17 08:01:10 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:01:08 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-17 08:00:19 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -36.000 |  |
| 2026-03-17 08:00:18 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -36.000 |  |
| 2026-03-17 07:18:49 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.014 |  |
| 2026-03-17 07:18:03 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-17 07:14:25 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 07:11:35 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.063 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 08:04:15 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-17 08:01:08 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-17 08:04:06 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-17 08:04:36 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 07:02:53 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.005 |  |
| 2026-03-17 07:08:04 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:01:10 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 07:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:02:15 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 07:01:14 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:03:19 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:02:16 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 07:05:39 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-03-17 07:18:03 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-17 07:07:04 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:05:04 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:02:43 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:03:18 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-17 07:05:24 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:03:17 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-17 07:14:25 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 08:01:53 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-17 07:00:38 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.002 |  |
| 2026-03-17 08:03:00 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-17 07:02:27 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-03-17 08:04:14 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-03-17 08:03:17 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-17 08:01:48 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-03-17 08:03:34 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-03-17 08:01:24 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.014 |  |
| 2026-03-17 08:04:00 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.020 |  |
| 2026-03-17 08:05:12 | Nagalagam Street (Kelani Ganga) | 0.17 | 🟢 Normal | -0.031 |  |
| 2026-03-17 08:05:18 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-03-17 07:11:35 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.063 |  |
| 2026-03-17 08:01:58 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.073 |  |
| 2026-03-17 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.081 |  |
| 2026-03-17 08:02:02 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.194 |  |
| 2026-03-16 18:00:13 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.210 |  |
| 2026-03-17 08:00:19 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)