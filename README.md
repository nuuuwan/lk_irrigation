# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_21:05:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,324 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 21:05:13 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.059 |  |
| 2026-06-06 21:04:56 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:48 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:39 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.021 |  |
| 2026-06-06 21:04:32 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-06-06 21:04:04 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:01 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:53 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:35 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:31 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-06-06 21:03:13 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-06 21:02:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:55 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.090 |  |
| 2026-06-06 21:02:52 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:16 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:14 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 21:02:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:32 | Ellagawa (Kalu Ganga) | 7.21 | 🟢 Normal | -0.040 |  |
| 2026-06-06 21:01:10 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 20:06:47 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-06 20:06:12 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-06 21:02:14 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 20:04:57 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 21:02:16 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:52 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:01 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:53 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:56 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:04 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:02:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:05:46 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:03:35 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:01:10 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 20:06:50 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:48 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-06 21:03:13 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-06 21:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.011 |  |
| 2026-06-06 21:04:32 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-06-06 20:03:27 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-06-06 20:06:31 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.020 |  |
| 2026-06-06 20:02:47 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-06-06 20:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.13 | 🟢 Normal | -0.021 |  |
| 2026-06-06 21:04:39 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.021 |  |
| 2026-06-06 20:08:55 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.028 |  |
| 2026-06-06 20:04:58 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.039 |  |
| 2026-06-06 21:01:32 | Ellagawa (Kalu Ganga) | 7.21 | 🟢 Normal | -0.040 |  |
| 2026-06-06 21:03:31 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-06-06 21:05:13 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.059 |  |
| 2026-06-06 20:07:22 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.067 |  |
| 2026-06-06 21:02:55 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)