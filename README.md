# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_20:21:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,130 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 20:21:48 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:10:28 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:09:55 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-02-14 20:09:48 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:09:34 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-02-14 20:09:34 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:09:33 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-02-14 20:09:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:06:52 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 20:06:35 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-02-14 20:05:40 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:05:17 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-14 20:05:05 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:04:52 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:03:34 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:03:28 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-14 20:03:27 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:03:18 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:55 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 20:02:53 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:49 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:46 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:46 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-02-14 20:02:38 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:33 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:30 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-02-14 20:02:30 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-14 20:02:11 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:01:59 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 20:01:43 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-02-14 20:01:30 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-02-14 20:01:22 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 20:01:43 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-02-14 20:09:34 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-02-14 20:03:28 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-14 20:05:17 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-14 20:02:30 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-14 20:01:59 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 20:02:55 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:02:04 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 20:06:52 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 20:02:49 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:53 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:03:34 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:11 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:10:28 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:21:48 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:03:27 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:09:34 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:01:22 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:05:05 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:33 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:38 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:02:46 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:09:48 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:10:54 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:03:18 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:04:52 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-14 20:09:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-02-14 19:10:36 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-02-14 20:09:33 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-02-14 20:02:46 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-02-14 20:02:30 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-02-14 20:01:30 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-02-14 19:01:06 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.025 |  |
| 2026-02-14 20:09:55 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-02-14 20:06:35 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-02-14 19:03:44 | Padiyathalawa (Maduru Oya) | 2.00 | 🟢 Normal | -0.685 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)