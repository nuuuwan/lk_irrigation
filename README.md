# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_00:08:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 00:08:39 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-14 00:08:18 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.056 |  |
| 2026-01-14 00:07:36 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-01-14 00:07:07 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:07:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-14 00:05:31 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:04:42 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.059 |  |
| 2026-01-14 00:04:10 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:04:07 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:04:03 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:03:53 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-14 00:03:41 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:03:32 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:03:23 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-14 00:03:07 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 00:02:56 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:02:55 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:02:53 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-14 00:02:42 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:02:41 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 00:02:31 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:02:23 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:02:03 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-14 00:01:48 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.035 |  |
| 2026-01-14 00:01:31 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:01:31 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:00:56 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-14 00:00:49 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-14 00:00:41 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:00:25 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-13 23:44:45 | Yaka Wewa (Ma Oya) | 1.13 | 🟢 Normal | -0.035 |  |
| 2026-01-13 23:24:33 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 23:22:09 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 00:00:49 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-13 23:08:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-14 00:08:39 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-14 00:00:56 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-14 00:03:53 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-13 22:22:35 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-14 00:03:07 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 00:02:41 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 00:07:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 23:02:48 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 23:02:36 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:01:31 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:00:25 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:02:23 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:04:03 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:54 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:07:07 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:03:41 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:05:31 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:02:55 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:02:56 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:00:41 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:02:31 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:02:42 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:04:07 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:03:32 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:01:31 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:04:10 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-13 23:13:39 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.005 |  |
| 2026-01-14 00:02:53 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-14 00:07:36 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-01-14 00:02:03 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-14 00:03:23 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-13 23:09:19 | Horowpothana (Yan Oya) | 3.79 | 🟢 Normal | -0.030 |  |
| 2026-01-14 00:01:48 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.035 |  |
| 2026-01-13 18:01:14 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.040 |  |
| 2026-01-14 00:08:18 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.056 |  |
| 2026-01-14 00:04:42 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)