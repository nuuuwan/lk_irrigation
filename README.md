# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_12:06:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,437 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 12:06:24 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:06:24 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.039 |  |
| 2026-06-30 12:06:20 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-30 12:05:59 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:05:40 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:05:39 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-06-30 12:04:53 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:04:16 | Ellagawa (Kalu Ganga) | 7.91 | 🟢 Normal | -0.021 |  |
| 2026-06-30 12:03:57 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | -0.020 |  |
| 2026-06-30 12:03:38 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.019 |  |
| 2026-06-30 12:03:21 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.091 |  |
| 2026-06-30 12:03:06 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-06-30 12:03:05 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-30 12:03:00 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-30 12:03:00 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:02:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 12:02:47 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.072 |  |
| 2026-06-30 12:02:40 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:02:39 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-30 12:02:39 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:02:37 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:02:24 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:02:16 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.039 |  |
| 2026-06-30 12:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.43 | 🟢 Normal | -0.070 |  |
| 2026-06-30 12:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:01:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:01:51 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.041 |  |
| 2026-06-30 12:01:24 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.020 |  |
| 2026-06-30 12:01:07 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:00:46 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:00:14 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 11:22:04 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 11:08:17 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.415 | 🔺 Rising |
| 2026-06-30 12:03:05 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-30 11:07:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-30 12:02:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 12:02:24 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:03:00 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:01:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 11:02:18 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:00:14 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:05:40 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:05:59 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:04:53 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:00:46 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:02:39 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:02:37 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-30 11:04:50 | Putupaula (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:01:07 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:02:40 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:06:24 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-30 12:02:39 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-30 11:06:55 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-30 12:06:20 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-30 12:05:39 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-06-30 12:03:06 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-06-30 12:03:00 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-30 12:03:38 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.019 |  |
| 2026-06-30 12:03:57 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | -0.020 |  |
| 2026-06-30 12:01:24 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.020 |  |
| 2026-06-30 12:04:16 | Ellagawa (Kalu Ganga) | 7.91 | 🟢 Normal | -0.021 |  |
| 2026-06-30 12:06:24 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.039 |  |
| 2026-06-30 11:06:57 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.039 |  |
| 2026-06-30 12:02:16 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.039 |  |
| 2026-06-30 12:01:51 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.041 |  |
| 2026-06-30 12:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.43 | 🟢 Normal | -0.070 |  |
| 2026-06-30 12:02:47 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.072 |  |
| 2026-06-30 12:03:21 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.091 |  |
| 2026-06-30 11:05:30 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.145 |  |
| 2026-06-30 11:05:06 | Rathnapura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)