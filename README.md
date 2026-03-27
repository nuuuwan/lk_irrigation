# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--27_08:06:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **108,574 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 08:06:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:05:46 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:05:42 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:05:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-27 08:04:31 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 08:04:29 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.011 |  |
| 2026-03-27 08:04:06 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:04:01 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:03:58 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-27 08:03:55 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:03:35 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:03:29 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-27 08:03:22 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:03:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.060 |  |
| 2026-03-27 08:02:41 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-03-27 08:02:31 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-03-27 08:02:22 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-27 08:02:14 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:02:08 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:02:04 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:01:35 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:01:28 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:01:14 | Ellagawa (Kalu Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-03-27 08:01:01 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-03-27 08:00:23 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 07:35:35 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-27 07:13:07 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-27 07:12:50 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 08:03:58 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-27 08:03:29 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-27 07:35:35 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-27 08:04:31 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 08:05:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-27 07:09:45 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-27 08:04:06 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:00:23 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 07:01:03 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:01:28 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:03:35 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 07:01:06 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-27 07:07:19 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-27 06:13:39 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 07:11:53 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:03:22 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:01:35 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:01:14 | Ellagawa (Kalu Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:05:46 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:03:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:06:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:04:01 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:02:08 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:05:42 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:03:55 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:02:04 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:02:14 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 07:13:07 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-27 07:10:17 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-27 08:02:22 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-27 08:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-03-27 08:04:29 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.011 |  |
| 2026-03-27 08:02:31 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-03-27 08:01:01 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-03-27 08:02:41 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-03-27 07:03:28 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.021 |  |
| 2026-03-27 07:09:38 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.027 |  |
| 2026-03-27 08:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.060 |  |
| 2026-03-27 07:10:18 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | -1.180 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)