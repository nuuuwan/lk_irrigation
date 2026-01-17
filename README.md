# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_21:04:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,367 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 21:04:38 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:04:38 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:04:19 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-01-17 21:04:09 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-01-17 21:04:08 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:03:33 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-01-17 21:03:25 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:03:19 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.013 |  |
| 2026-01-17 21:03:18 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:03:16 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-17 21:03:00 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-17 21:02:59 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:57 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:29 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:03 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:00 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 21:01:45 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:01:21 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.012 |  |
| 2026-01-17 21:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-17 21:01:05 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:01:01 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.042 |  |
| 2026-01-17 20:33:34 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-01-17 20:15:39 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.013 |  |
| 2026-01-17 20:13:27 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 20:11:45 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 20:11:45 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-01-17 20:10:24 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.018 |  |
| 2026-01-17 20:09:19 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 21:03:33 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-01-17 21:03:00 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-17 21:02:00 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 21:02:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:03:25 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:03:18 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:29 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 20:13:27 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 18:02:19 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:04:08 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:57 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 20:33:34 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:01:45 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:59 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:01:05 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:04:38 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:02:03 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-17 20:06:38 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 20:06:13 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-17 20:11:45 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 20:02:29 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:04:38 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 21:03:16 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-17 20:03:00 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-17 20:04:09 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-17 21:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-17 21:04:09 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-01-17 21:01:21 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.012 |  |
| 2026-01-17 21:03:19 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.013 |  |
| 2026-01-17 20:10:24 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.018 |  |
| 2026-01-17 18:02:02 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-17 20:05:48 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2026-01-17 20:04:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | -0.029 |  |
| 2026-01-17 18:01:12 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.040 |  |
| 2026-01-17 20:02:17 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.040 |  |
| 2026-01-17 21:01:01 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.042 |  |
| 2026-01-17 20:05:32 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.051 |  |
| 2026-01-17 21:04:19 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)