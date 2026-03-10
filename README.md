# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_08:29:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,174 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 08:29:15 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:20:33 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-03-10 08:14:37 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:12:30 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | -0.008 |  |
| 2026-03-10 08:11:44 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:10:13 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:09:10 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:08:51 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:07:30 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:06:24 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:06:04 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:05:26 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-10 08:04:41 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-10 08:04:08 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.122 |  |
| 2026-03-10 08:04:01 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-03-10 08:03:37 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-10 08:03:35 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:03:32 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:03:25 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-10 08:03:10 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.069 |  |
| 2026-03-10 08:02:34 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-03-10 08:02:32 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 08:02:25 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:02:25 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:02:17 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:02:16 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:02:12 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-10 08:02:06 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:01:54 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.150 |  |
| 2026-03-10 08:01:50 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:01:44 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.082 |  |
| 2026-03-10 08:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:01:13 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:01:10 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.022 |  |
| 2026-03-10 08:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-10 08:01:02 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:00:53 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-03-10 08:00:11 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 08:02:12 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-10 08:04:41 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-10 08:02:32 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 08:01:05 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-10 08:02:16 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:01:13 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:07:30 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:02:25 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:03:32 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:29:15 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:19:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:09:10 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:06:04 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:10:13 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:01:50 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:14:37 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:06:24 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:00:11 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:01:02 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:08:51 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:02:25 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:02:06 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:03:10 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:11:44 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:02:17 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 08:12:30 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | -0.008 |  |
| 2026-03-10 08:05:26 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-10 08:04:01 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-03-10 08:03:25 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-10 08:00:53 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-03-10 08:03:37 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-03-10 08:02:34 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-03-10 08:01:10 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.022 |  |
| 2026-03-10 08:20:33 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-03-10 08:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.069 |  |
| 2026-03-10 08:01:44 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.082 |  |
| 2026-03-10 08:04:08 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.122 |  |
| 2026-03-10 08:01:54 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)