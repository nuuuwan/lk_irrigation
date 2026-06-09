# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_12:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,641 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 12:03:31 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.040 |  |
| 2026-06-09 12:03:15 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:03:06 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:03:01 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.029 |  |
| 2026-06-09 12:02:58 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:02:53 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:02:38 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-09 12:02:17 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-09 12:01:27 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.032 |  |
| 2026-06-09 12:01:16 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | -0.010 |  |
| 2026-06-09 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-09 12:01:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:00:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 11:33:55 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:16:04 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:14:22 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:13:19 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:13:18 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:12:10 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 12:01:10 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-06-09 11:04:31 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-09 12:00:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 12:03:15 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:01:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:02:17 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:33:55 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:00:40 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:05:53 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:02:53 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:03:02 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:12:10 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:03:06 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-09 12:02:58 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:07:05 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:16:04 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:14:22 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:02:12 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-09 11:06:58 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-06-09 11:04:59 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-09 12:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-09 11:05:44 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | -0.010 |  |
| 2026-06-09 12:01:16 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | -0.010 |  |
| 2026-06-09 12:02:38 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-06-09 11:01:36 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-09 11:10:20 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.018 |  |
| 2026-06-09 11:01:07 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-06-09 11:01:55 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2026-06-09 11:04:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | -0.021 |  |
| 2026-06-09 11:03:38 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.022 |  |
| 2026-06-09 11:05:51 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.023 |  |
| 2026-06-09 12:03:01 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.029 |  |
| 2026-06-09 11:03:05 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.030 |  |
| 2026-06-09 11:03:48 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-06-09 12:01:27 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.032 |  |
| 2026-06-09 11:06:38 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.037 |  |
| 2026-06-09 12:03:31 | Hanwella (Kelani Ganga) | 3.33 | 🟢 Normal | -0.040 |  |
| 2026-06-09 11:04:39 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-06-09 11:02:33 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)