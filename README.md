# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_04:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,229 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 04:13:08 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.005 |  |
| 2026-06-10 04:09:43 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.047 |  |
| 2026-06-10 04:07:41 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.024 |  |
| 2026-06-10 04:06:45 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.013 |  |
| 2026-06-10 04:06:15 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:06:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:05:27 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:05:26 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-06-10 04:05:19 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:04:43 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.061 |  |
| 2026-06-10 04:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-06-10 04:04:33 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.008 |  |
| 2026-06-10 04:04:04 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:03:39 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2026-06-10 04:03:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:03:32 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 04:03:19 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-10 04:02:34 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-10 04:02:28 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-10 04:02:13 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:02:06 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 04:01:30 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.020 |  |
| 2026-06-10 04:01:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-10 04:01:02 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 04:00:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:40:01 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 04:03:19 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-10 04:01:02 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-10 04:02:06 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 04:03:32 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-10 04:04:04 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:02:13 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:00:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:04:47 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:06:15 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:02:55 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:03:19 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:12:02 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:05:27 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-06-10 02:05:44 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:06:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:03:57 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:03:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:05:19 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-06-09 18:12:11 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-10 02:02:28 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-10 02:01:09 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 03:00:44 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 04:13:08 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.005 |  |
| 2026-06-10 04:04:33 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.008 |  |
| 2026-06-10 04:02:28 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-10 04:02:34 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-10 04:01:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-10 01:03:39 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.011 |  |
| 2026-06-10 04:06:45 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.013 |  |
| 2026-06-10 04:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-06-10 04:05:26 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-06-10 04:01:30 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.020 |  |
| 2026-06-10 03:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.023 |  |
| 2026-06-10 04:07:41 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.024 |  |
| 2026-06-09 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.031 |  |
| 2026-06-10 04:03:39 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2026-06-10 04:09:43 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.047 |  |
| 2026-06-10 03:04:39 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.058 |  |
| 2026-06-10 04:04:43 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)