# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--17_13:46:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **75,519 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 13:46:21 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.006 |  |
| 2026-02-17 13:23:35 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:18:37 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 3.189 | 🔺 Rising |
| 2026-02-17 13:14:16 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:12:34 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:10:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-17 13:10:08 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-17 13:09:11 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-17 13:08:15 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-17 13:07:24 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:07:06 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:06:34 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-17 13:06:19 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:05:43 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:04:53 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 3.189 | 🔺 Rising |
| 2026-02-17 13:04:30 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-02-17 13:04:04 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.040 |  |
| 2026-02-17 13:03:54 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:03:45 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:03:36 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-17 13:03:27 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-17 13:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-17 13:02:45 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 28.577 | 🔺 Rising |
| 2026-02-17 13:02:37 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:02:25 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:02:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:02:23 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-17 13:02:19 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:02:16 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:02:11 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-17 13:01:59 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:01:55 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-02-17 13:01:55 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 13:01:53 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:01:11 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 13:01:09 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.064 |  |
| 2026-02-17 13:01:08 | Peradeniya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 28.577 | 🔺 Rising |
| 2026-02-17 13:00:54 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:00:06 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-17 13:02:45 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 28.577 | 🔺 Rising |
| 2026-02-17 13:18:37 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 3.189 | 🔺 Rising |
| 2026-02-17 13:04:30 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-02-17 13:10:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-17 13:06:34 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-17 13:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-17 13:02:23 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-17 13:01:55 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-17 13:08:15 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-17 13:03:36 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-17 13:01:11 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-17 13:02:37 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:00:06 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:02:25 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-17 12:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:01:53 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:05:43 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:07:06 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:02:19 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:14:16 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:12:34 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:00:54 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:02:16 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:06:19 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:03:54 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:03:45 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:07:24 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:01:59 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:23:35 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:02:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-17 13:46:21 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.006 |  |
| 2026-02-17 13:10:08 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-02-17 13:09:11 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-17 13:03:27 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-17 13:02:11 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-17 13:01:55 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-02-17 11:09:28 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-02-17 13:04:04 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.040 |  |
| 2026-02-17 13:01:09 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)