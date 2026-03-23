# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--23_08:05:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,995 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 08:05:25 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:05:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.024 |  |
| 2026-03-23 08:04:23 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:04:20 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:04:20 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-03-23 08:04:19 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:04:06 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-03-23 08:03:47 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.125 |  |
| 2026-03-23 08:03:45 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:03:40 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:03:26 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-23 08:03:22 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.039 |  |
| 2026-03-23 08:03:18 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.048 |  |
| 2026-03-23 08:03:17 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.125 |  |
| 2026-03-23 08:03:16 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-03-23 08:03:05 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-23 08:02:55 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.040 |  |
| 2026-03-23 08:02:52 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:38 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:37 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 08:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.060 |  |
| 2026-03-23 08:02:23 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:15 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:10 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:09 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:01:47 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:01:46 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:01:36 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:00:12 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:00:10 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:00:08 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 07:31:54 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-23 07:28:40 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-23 07:14:22 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 07:06:08 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-23 08:03:26 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-23 08:03:05 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-23 07:02:53 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 07:02:39 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 08:02:37 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 08:01:47 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:00:08 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 07:03:14 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:23 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:00:12 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:00:10 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 07:07:12 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:01:36 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:52 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:05:25 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:01:46 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:04:23 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:09 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:38 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:10 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:03:40 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-03-23 07:14:22 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:03:45 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:02:15 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-23 07:02:44 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-23 08:03:16 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-03-23 08:04:06 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-03-23 07:04:45 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.013 |  |
| 2026-03-23 08:04:20 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-03-23 08:05:05 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.024 |  |
| 2026-03-23 07:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-03-23 08:03:22 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.039 |  |
| 2026-03-23 08:02:55 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.040 |  |
| 2026-03-23 08:03:18 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.048 |  |
| 2026-03-23 07:03:54 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.058 |  |
| 2026-03-23 08:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.060 |  |
| 2026-03-23 08:03:17 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.125 |  |
| 2026-03-23 08:03:47 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)