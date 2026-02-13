# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_03:13:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,473 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 03:13:01 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:12:31 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:11:27 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.094 |  |
| 2026-02-14 03:10:05 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:07:33 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.006 |  |
| 2026-02-14 03:06:35 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-02-14 03:06:24 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-14 03:06:24 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:05:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.029 |  |
| 2026-02-14 03:05:39 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 03:05:01 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | -0.005 |  |
| 2026-02-14 03:04:28 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-14 03:04:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-14 03:04:19 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:03:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-14 03:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-02-14 03:03:34 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-14 03:03:16 | Giriulla (Maha Oya) | 0.50 | 🟢 Normal | -0.211 |  |
| 2026-02-14 03:03:13 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.014 |  |
| 2026-02-14 03:02:55 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:02:53 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:02:53 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.151 |  |
| 2026-02-14 03:02:19 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-14 03:02:14 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.348 |  |
| 2026-02-14 03:01:50 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:01:41 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:01:31 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:01:20 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:01:19 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:01:16 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.040 |  |
| 2026-02-14 03:01:04 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 03:00:48 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-14 03:00:39 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -0.003 |  |
| 2026-02-14 02:56:17 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:47:38 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.037 |  |
| 2026-02-14 02:45:05 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-14 02:33:11 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.094 |  |
| 2026-02-14 02:19:35 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.014 |  |
| 2026-02-14 02:18:26 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.014 |  |
| 2026-02-14 02:18:05 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 03:03:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-14 03:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-02-14 02:45:05 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-14 03:04:28 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-14 03:05:39 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 03:01:04 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 03:01:50 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:01:41 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:01:19 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:06:24 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-14 02:16:51 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:04:19 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:01:20 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:02:53 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:02:55 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:12:31 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:10:05 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:13:01 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 03:00:39 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | -0.003 |  |
| 2026-02-14 03:05:01 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | -0.005 |  |
| 2026-02-14 03:07:33 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.006 |  |
| 2026-02-14 03:06:24 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-14 03:02:19 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-14 01:00:26 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-14 03:04:27 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-02-14 03:00:48 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-14 03:03:13 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.014 |  |
| 2026-02-14 03:05:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.029 |  |
| 2026-02-14 03:06:35 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-02-14 02:47:38 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.037 |  |
| 2026-02-14 03:01:16 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.040 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-14 03:11:27 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.094 |  |
| 2026-02-14 03:02:53 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.151 |  |
| 2026-02-14 03:03:16 | Giriulla (Maha Oya) | 0.50 | 🟢 Normal | -0.211 |  |
| 2026-02-14 03:02:14 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.348 |  |
| 2026-02-14 02:06:11 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.742 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)