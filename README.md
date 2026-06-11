# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_22:06:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,824 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 22:06:07 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-11 22:05:52 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:05:44 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-06-11 22:05:34 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-06-11 22:04:27 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-11 22:04:27 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-06-11 22:03:21 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-06-11 22:02:54 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-11 22:02:54 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:44 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-11 22:02:41 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-11 22:02:35 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-11 22:02:24 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:18 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:11 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-11 22:02:08 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:07 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-11 22:02:02 | Deraniyagala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.163 |  |
| 2026-06-11 22:01:50 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | 0.399 | 🔺 Rising |
| 2026-06-11 22:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:01:10 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:00:50 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:00:44 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:00:26 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-06-11 21:18:53 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.055 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 21:05:26 | Rathnapura (Kalu Ganga) | 5.03 | 🟢 Normal | 1.017 | 🔺 Rising |
| 2026-06-11 22:01:50 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | 0.399 | 🔺 Rising |
| 2026-06-11 22:04:27 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-06-11 22:03:21 | Glencourse (Kelani Ganga) | 11.63 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-06-11 22:05:34 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-06-11 22:06:07 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-11 21:02:18 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-06-11 21:01:20 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-11 22:04:27 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-11 21:05:14 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-06-11 22:02:35 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-11 22:02:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-11 22:02:54 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-11 22:02:41 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-11 22:02:44 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-11 21:04:02 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-11 21:09:01 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 22:02:11 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-11 21:08:18 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 22:02:24 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:01:10 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:54 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:00:44 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:11:49 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:05:52 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:18 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:00:50 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 21:04:01 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:08 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:02:07 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-11 21:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 22:00:26 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-06-11 22:05:44 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-06-11 18:00:24 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.021 |  |
| 2026-06-11 21:01:54 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.048 |  |
| 2026-06-11 22:02:02 | Deraniyagala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)