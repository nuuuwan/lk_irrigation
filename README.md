# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_17:11:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,858 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 17:11:44 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-25 17:11:21 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:09:08 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-02-25 17:07:39 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:07:39 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:07:18 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:07:08 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.021 |  |
| 2026-02-25 17:06:42 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:04:43 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.011 |  |
| 2026-02-25 17:04:38 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:03:48 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:03:29 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:03:25 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:03:23 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:03:16 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:03:13 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:03:02 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-02-25 17:03:01 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-02-25 17:02:46 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:45 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:41 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:39 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.040 |  |
| 2026-02-25 17:02:19 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:02:18 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:02:14 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-02-25 17:02:08 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:02:07 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:01 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:01:50 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:01:28 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.011 |  |
| 2026-02-25 17:01:23 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | -0.060 |  |
| 2026-02-25 17:01:14 | Thawalama (Gin Ganga) | 0.39 | 🟢 Normal | -0.836 |  |
| 2026-02-25 17:01:03 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:00:48 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:00:43 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:57:55 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 17:02:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-02-25 17:09:08 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-02-25 16:57:55 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-25 17:11:44 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-25 17:02:39 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:01:50 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:01 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:03:29 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:41 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:00:43 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:07:39 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-25 16:10:30 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:03:13 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:03:23 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:11:21 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:45 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:07:39 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:07 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:00:48 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:03:16 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:06:42 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:03:25 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 17:02:08 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:07:18 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:03:48 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:02:19 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:01:03 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:02:18 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:04:38 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:03:01 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-02-25 17:01:28 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.011 |  |
| 2026-02-25 17:04:43 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.011 |  |
| 2026-02-25 17:03:02 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-02-25 17:02:14 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-02-25 17:07:08 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.021 |  |
| 2026-02-25 17:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.040 |  |
| 2026-02-25 17:01:23 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | -0.060 |  |
| 2026-02-25 17:01:14 | Thawalama (Gin Ganga) | 0.39 | 🟢 Normal | -0.836 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)