# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_13:47:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,020 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 13:47:45 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.024 |  |
| 2026-05-10 13:14:49 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-05-10 13:14:41 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-05-10 13:11:21 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:09:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:06:35 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.028 |  |
| 2026-05-10 13:06:35 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.085 |  |
| 2026-05-10 13:06:05 | Katharagama (Menik Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:05:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:05:31 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:05:27 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:05:25 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.040 |  |
| 2026-05-10 13:05:08 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | -0.058 |  |
| 2026-05-10 13:05:05 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:04:50 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.019 |  |
| 2026-05-10 13:04:01 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:03:21 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:03:16 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-10 13:02:58 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.099 |  |
| 2026-05-10 13:02:48 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-10 13:02:41 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 13:01:44 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-10 13:02:15 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-10 13:01:36 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:05:31 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:05:05 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:02:14 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:00:26 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:05:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:04:01 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:06:05 | Katharagama (Menik Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:05:27 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:00:42 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:03:21 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:11:21 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:09:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-10 13:14:49 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-05-10 13:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-10 13:01:38 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-10 13:03:16 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-10 13:02:48 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-05-10 13:02:26 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-05-10 13:14:41 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.017 |  |
| 2026-05-10 13:04:50 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.019 |  |
| 2026-05-10 13:02:41 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-05-10 13:02:16 | Kuda Oya (Kirindi Oya) | 1.96 | 🟢 Normal | -0.022 |  |
| 2026-05-10 13:47:45 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.024 |  |
| 2026-05-10 13:06:35 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.028 |  |
| 2026-05-10 13:01:18 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.029 |  |
| 2026-05-10 12:01:58 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.040 |  |
| 2026-05-10 13:05:25 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.040 |  |
| 2026-05-10 13:01:31 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | -0.050 |  |
| 2026-05-10 13:02:29 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.050 |  |
| 2026-05-10 13:05:08 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | -0.058 |  |
| 2026-05-10 13:01:59 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.080 |  |
| 2026-05-10 13:02:28 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.082 |  |
| 2026-05-10 13:06:35 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.085 |  |
| 2026-05-10 13:02:10 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.092 |  |
| 2026-05-10 13:02:58 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.099 |  |
| 2026-05-10 13:02:29 | Moragaswewa (Deduru Oya) | 2.04 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)