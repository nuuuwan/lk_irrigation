# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_08:04:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **204,039 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 08:04:46 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-07-12 08:04:15 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.029 |  |
| 2026-07-12 08:03:44 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.063 |  |
| 2026-07-12 08:03:44 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-07-12 08:03:40 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:03:17 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:03:14 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:55 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:47 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:42 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:39 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:36 | Putupaula (Kalu Ganga) | 0.14 | 🟢 Normal | -0.032 |  |
| 2026-07-12 08:02:35 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:16 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:15 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.020 |  |
| 2026-07-12 08:02:13 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-12 08:02:09 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:09 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-07-12 08:01:27 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.061 |  |
| 2026-07-12 08:00:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:00:37 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:58:38 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:17:02 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:17:01 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 08:02:09 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-07-12 08:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-07-12 07:01:59 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 07:07:08 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 08:02:09 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:39 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:55 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:03:17 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:03:14 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:00:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:17:02 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:11:37 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:02:51 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:16 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:16:36 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:47 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:42 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:03:40 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:00:37 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:03:50 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:05:26 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:35 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:12:48 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:04:46 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:58:38 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-12 08:02:13 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-12 08:03:44 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-07-12 07:02:21 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-07-12 07:02:50 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-07-12 07:04:59 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-07-12 08:02:15 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.020 |  |
| 2026-07-12 07:03:02 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | -0.027 |  |
| 2026-07-12 08:04:15 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.029 |  |
| 2026-07-12 07:07:58 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.029 |  |
| 2026-07-12 08:02:36 | Putupaula (Kalu Ganga) | 0.14 | 🟢 Normal | -0.032 |  |
| 2026-07-12 07:08:34 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.046 |  |
| 2026-07-12 08:01:27 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.061 |  |
| 2026-07-12 08:03:44 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)