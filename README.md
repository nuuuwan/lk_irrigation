# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_11:19:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,990 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 11:19:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.029 |  |
| 2026-04-12 11:12:47 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:11:20 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:10:56 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.025 |  |
| 2026-04-12 11:09:56 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:08:52 | Nawalapitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-04-12 11:08:38 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.023 |  |
| 2026-04-12 11:08:20 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:08:20 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-04-12 11:07:10 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-12 11:07:01 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.043 |  |
| 2026-04-12 11:06:26 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-04-12 11:06:05 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:05:03 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:04:35 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-12 11:04:09 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:04:00 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 11:01:20 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-04-12 11:02:30 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-04-12 11:04:35 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-04-12 11:04:00 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 11:03:11 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-12 10:10:12 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 11:00:14 | Weraganthota (Mahaweli Ganga) | -2.29 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:04:09 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:03:04 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:01:57 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:06:05 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:00:42 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:03:35 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:05:03 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:12:47 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:03:37 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:08:20 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:00:18 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:00:18 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:02:31 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:00:47 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:00:18 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:09:56 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:11:20 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 11:08:52 | Nawalapitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-04-12 11:06:26 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-04-12 11:07:10 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-04-12 11:08:20 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-04-12 11:03:06 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-12 11:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-12 11:02:52 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-12 11:01:08 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-12 11:01:22 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-04-12 11:08:38 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.023 |  |
| 2026-04-12 11:10:56 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.025 |  |
| 2026-04-12 11:02:14 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.028 |  |
| 2026-04-12 11:19:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.029 |  |
| 2026-04-12 11:07:01 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.043 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)