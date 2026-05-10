# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_22:02:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,345 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 22:02:24 | Thanamalwila (Kirindi Oya) | 2.89 | 🟢 Normal | 0.956 | 🔺 Rising |
| 2026-05-10 22:02:24 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-10 22:02:13 | Katharagama (Menik Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-10 22:02:13 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:02:10 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:02:05 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 22:01:40 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.042 |  |
| 2026-05-10 22:01:35 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.021 |  |
| 2026-05-10 22:01:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2026-05-10 22:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-10 22:01:18 | Kuda Oya (Kirindi Oya) | 4.41 | 🟢 Normal | 1.417 | 🔺 Rising |
| 2026-05-10 22:01:10 | Wellawaya (Kirindi Oya) | 4.04 | 🟢 Normal | 0.689 | 🔺 Rising |
| 2026-05-10 22:01:08 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-10 22:01:05 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:00:59 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:00:51 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.035 |  |
| 2026-05-10 21:18:22 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-10 21:14:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.077 |  |
| 2026-05-10 21:12:00 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 22:01:18 | Kuda Oya (Kirindi Oya) | 4.41 | 🟢 Normal | 1.417 | 🔺 Rising |
| 2026-05-10 22:02:24 | Thanamalwila (Kirindi Oya) | 2.89 | 🟢 Normal | 0.956 | 🔺 Rising |
| 2026-05-10 22:01:10 | Wellawaya (Kirindi Oya) | 4.04 | 🟢 Normal | 0.689 | 🔺 Rising |
| 2026-05-10 22:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-10 21:07:01 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-10 22:01:08 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-05-10 22:02:24 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-10 21:05:14 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-10 21:02:28 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-10 21:00:38 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-10 21:02:12 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-10 22:02:13 | Katharagama (Menik Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-10 22:02:05 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-10 21:02:24 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-10 21:05:27 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 21:18:22 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-10 22:02:10 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:04:59 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:01:05 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-10 22:00:59 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:10:00 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:02:52 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-10 21:04:58 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:08:34 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-10 22:02:13 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-05-10 21:04:25 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-10 22:01:35 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.021 |  |
| 2026-05-10 21:02:26 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-05-10 21:07:21 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-05-10 22:01:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2026-05-10 21:12:00 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.035 |  |
| 2026-05-10 22:00:51 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.035 |  |
| 2026-05-10 21:01:55 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.035 |  |
| 2026-05-10 21:06:53 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-05-10 22:01:40 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.042 |  |
| 2026-05-10 21:14:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)