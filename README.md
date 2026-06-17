# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_09:12:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,679 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 09:12:00 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.005 |  |
| 2026-06-17 09:10:59 | Yaka Wewa (Ma Oya) | 1.37 | 🟢 Normal | 5.533 | 🔺 Rising |
| 2026-06-17 09:09:36 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-06-17 09:09:11 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 09:07:13 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:07:11 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:07:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-06-17 09:06:33 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:06:11 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:05:36 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:05:15 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.012 |  |
| 2026-06-17 09:05:09 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:04:26 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:04:24 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.020 |  |
| 2026-06-17 09:04:16 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:04:00 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-06-17 09:03:57 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.040 |  |
| 2026-06-17 09:03:57 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-06-17 09:03:39 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:03:35 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:03:15 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-17 09:03:11 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.049 |  |
| 2026-06-17 09:03:07 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.033 |  |
| 2026-06-17 09:03:03 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.024 |  |
| 2026-06-17 09:02:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:02:55 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:02:52 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:02:35 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.024 |  |
| 2026-06-17 09:02:33 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:02:25 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 09:02:24 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:02:08 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.158 |  |
| 2026-06-17 09:02:03 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-06-17 09:02:03 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:01:50 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:01:46 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 5.533 | 🔺 Rising |
| 2026-06-17 09:01:08 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-17 09:01:04 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:00:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:00:22 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.052 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 09:10:59 | Yaka Wewa (Ma Oya) | 1.37 | 🟢 Normal | 5.533 | 🔺 Rising |
| 2026-06-17 09:09:36 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.397 | 🔺 Rising |
| 2026-06-17 09:01:08 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-17 09:02:25 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 09:09:11 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-17 09:01:50 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:00:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:07:11 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:04:16 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:04:26 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:03:39 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:06:33 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:02:56 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:02:03 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:05:09 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:02:52 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:07:13 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:06:11 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 09:12:00 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.005 |  |
| 2026-06-17 09:05:36 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:02:33 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:02:24 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:03:35 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:02:55 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-17 09:03:57 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-06-17 09:05:15 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.012 |  |
| 2026-06-17 09:04:00 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-06-17 09:04:24 | Hanwella (Kelani Ganga) | 1.97 | 🟢 Normal | -0.020 |  |
| 2026-06-17 09:03:15 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-06-17 09:03:03 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.024 |  |
| 2026-06-17 09:02:35 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.024 |  |
| 2026-06-17 09:07:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.028 |  |
| 2026-06-17 09:03:07 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.033 |  |
| 2026-06-17 09:03:57 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.040 |  |
| 2026-06-17 09:03:11 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.049 |  |
| 2026-06-17 09:00:22 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.052 |  |
| 2026-06-17 09:02:08 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)